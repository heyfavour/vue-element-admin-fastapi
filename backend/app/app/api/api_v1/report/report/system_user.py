from  app.api.api_v1.report.gen_excel import gen_template

class Query():
    def __init__(self):
        self.header = ["用户编号","用户姓名","部门","性别"]
        self.file_name  = "员工信息"

    def get_template(self):
        return gen_template(self.header,self.file_name)





