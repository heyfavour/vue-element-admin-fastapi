from app.api.api_v1.report.gen_report import BaseQuery
from app import models
from app.extensions.utils import list_to_tree


class Query(BaseQuery):
    def report_config(self):
        self.header = ["用户编号", "用户昵称", "部门", "身份证", "手机号码", "性别", "状态", "岗位"]
        self.file_name = "员工信息"

    def instance_data(self):
        post = self.db.query(models.User_Dict.user_id.label("user_id"), models.Dict_Data.label.label("post")).join(
            models.Dict_Data, models.Dict_Data.id == models.User_Dict.dict_id).join(
            models.Dict_Type, models.Dict_Type.id == models.Dict_Data.type_id).filter(
            models.Dict_Type.code == "post").subquery()

        query = self.db.query(models.User, models.Department, post).outerjoin(
            models.User_Department, models.User_Department.user_id == models.User.id).outerjoin(
            models.Department, models.Department.id == models.User_Department.department_id).outerjoin(
            post, post.c.user_id == models.User.id)

        if self.query_params.get("username"):
            query = query.filter(models.User.username.like("%" + self.query_params.get("username") + "%"))
        if self.query_params.get("nickname"): query = query.filter(
            models.User.nickname.like("%" + self.query_params.get("nickname") + "%"))
        if self.query_params.get("nickname"): query = query.filter(
            models.User.status == self.query_params.get("status"))
        # 根据部门ID筛选部门及部门下级所有员工
        if self.query_params.get("deptId"):
            departments = self.db.query(models.Department).filter(
                models.Department.id,models.Department.status == 1).all()
            tree = list_to_tree([dep.dict() for dep in departments], root_id=self.query_params.get("deptId"))

            # 递归获取部门及部门下级
            def get_list_id_by_tree(nodes):
                ids = [nodes["id"], ]
                if nodes.get("children"):
                    for node in nodes["children"]: ids = ids + get_list_id_by_tree(node)
                return ids

            tree_ids = get_list_id_by_tree(tree)
            query = query.filter(models.User_Department.department_id.in_(tree_ids))
        rows = query.all()
        data = []
        for row in rows:
            data_row = [
                row.User.username,
                row.User.nickname,
                row.Department.name,
                row.User.identity_card,
                row.User.phone,
                row.User.sex,
                row.User.status,
                row[3]
            ]
            data.append(data_row)
        return data
