from typing import Any, Dict, Optional,List

from fastapi import APIRouter, Depends, HTTPException,Body,Request
from sqlalchemy.orm import Session,joinedload_all,contains_eager,Load
from fastapi.encoders import jsonable_encoder
from app import crud, models, schemas
from app.api import deps
from app.core.security import get_password_hash

from app.utils import list_to_tree,get_list_id_by_tree

router = APIRouter()


@router.get("/me", response_model= schemas.Response)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.
    User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    user = current_user.dict()
    user['roles'] = [role.role.key for role in current_user.roles]
    return {
        "code": 20000,
        "data": user,
        "message":"",
    }

@router.get("/list", response_model=schemas.Response)
def read_routes(*,
                db: Session = Depends(deps.get_db),
                limit:int,page:int,
                deptId:Optional[int]=None,username:Optional[str]=None,nickname:Optional[str]=None,status:Optional[str]=None,
                current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    query = db.query(models.User,models.Department
                    ).outerjoin(models.User_Department,models.User_Department.user_id == models.User.id
                    ).outerjoin(models.Department,models.Department.id == models.User_Department.department_id)
    if username:query  = query.filter(models.User.username.like("%" + username + "%") )
    if nickname:query = query.filter(models.User.nickname.like("%" + username + "%") )
    if status:query = query.filter(models.User.status == status )
    if deptId:
        depts = db.query(models.Department).filter(models.Department.id, models.Department.status == 1).all()
        tree = list_to_tree([dep.dict() for dep in depts], deptId)
        tree_ids = get_list_id_by_tree(tree)
        query = query.filter(models.User_Department.department_id.in_(tree_ids))
    total = query.count()
    user_list = []
    items = query.limit(limit).offset((page - 1) * limit).all()
    for u in items:
        user = u[0].dict()
        user["dept"] = u[1]
        user_list.append(user)
    return {
        "code": 20000,
        "data": {
            "items": user_list,
            'total': total
        },
        "message": "修改成功",
    }
@router.get("/",response_model=schemas.Response)
def read_user(*,db: Session = Depends(deps.get_db),current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    roleOptions = db.query(models.Role).all()
    postOptions = db.query(models.Dict_Data).join(models.Dict_Type,models.Dict_Type.id == models.Dict_Data.type_id).filter(models.Dict_Type.code == "post").all()
    return {
        "code": 20000,
        "data": {
            "roleOptions":roleOptions,
            "postOptions":postOptions,
        },
        "message": "修改成功",
    }

@router.get("/{id}",response_model=schemas.Response)
def read_user(*,db: Session = Depends(deps.get_db),id:int,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    roleOptions = db.query(models.Role).all()
    postOptions = db.query(models.Dict_Data).join(models.Dict_Type,models.Dict_Type.id == models.Dict_Data.type_id).filter(models.Dict_Type.code == "post").all()
    user = db.query(models.User).filter(models.User.id == id).one()
    user_department = db.query(models.User_Department).filter(models.User_Department.user_id == id).first()
    user_role = db.query(models.User_Role).filter(models.User_Role.user_id == id).all()
    user_post = db.query(models.User_Dict
                         ).outerjoin(models.Dict_Data, models.Dict_Data.id == models.User_Dict.dict_id
                         ).outerjoin(models.Dict_Type,models.Dict_Type.id == models.Dict_Data.type_id
                         ).filter(models.Dict_Type.code=="post",models.User_Dict.user_id == id).all()

    user = user.dict()
    user["deptId"]  = user_department.department_id
    user["roleIds"] = [r.role.id for r in user_role]
    user["postIds"] = [up.dict_id for up in user_post]
    return {
        "code": 20000,
        "data": {
            "user":user,
            "roleOptions":roleOptions,
            "postOptions":postOptions,
        },
        "message": "修改成功",
    }


@router.put("/",response_model=schemas.Response)
def update_user(*,db: Session = Depends(deps.get_db),user:schemas.UserUpdate,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    user_id = user.id
    user_data = {
        "username":user.username,
        "nickname":user.nickname,
        "identity_card":user.identity_card,
        "phone":user.phone,
        "address":user.address,
        "sex":user.sex,
        "work_start":user.work_start,
        "avatar":user.avatar,
        "introduction":user.introduction,
        "is_active":user.is_active,
        "is_superuser":user.is_superuser,
        "status":user.status,
    }
    deptId = user.deptId
    postIds = user.postIds
    roleIds = user.roleIds
    #info
    db.query(models.User).filter(models.User.id == user_id).update(user_data)
    db.flush()
    #department
    db.query(models.User_Department).filter(models.User_Department.user_id == user_id).delete()
    user_department = {
        "user_id":user_id,
        "department_id":deptId,
    }
    db.add(models.User_Department(**user_department))
    db.flush()
    #dcit
    #post
    db.query(models.User_Dict).filter(models.User_Dict.user_id == user_id).delete()
    user_post = [{"user_id":user_id,"dict_id":i} for i in postIds]
    user_dict = user_post + []
    db.bulk_insert_mappings(models.User_Dict,user_dict)
    db.flush()
    #role
    db.query(models.User_Role).filter(models.User_Role.user_id == user_id).delete()
    user_roles = [{"user_id": user_id, "role_id": i} for i in roleIds]
    db.bulk_insert_mappings(models.User_Role,user_roles)
    db.flush()
    return {
        "code": 20000,
        "data": "",
        "message": "修改成功",
    }


@router.post("/", response_model=schemas.Response)
def add_user(*, db: Session = Depends(deps.get_db), user: schemas.UserCreate,
             current_user: models.User = Depends(deps.get_current_active_user)
             ) -> Any:
    user_data = {
        "username":user.username,
        "nickname":user.nickname,
        "identity_card":user.identity_card,
        "phone":user.phone,
        "address":user.address,
        "sex":user.sex,
        "hashed_password":get_password_hash("qwe123"),
        "introduction":user.introduction,
        "is_active":True,
        "is_superuser":False,
        "status":user.status,
    }
    add_user = models.User(**user_data)
    db.add(add_user)
    db.flush()

    deptId = user.deptId
    postIds = user.postIds
    roleIds = user.roleIds
    #department
    user_department = {
        "user_id":add_user.id,
        "department_id":deptId,
    }
    db.add(models.User_Department(**user_department))
    db.flush()
    # dict
    # post
    user_post = [{"user_id":add_user.id,"dict_id":i} for i in postIds]
    user_dict = user_post + []
    db.bulk_insert_mappings(models.User_Dict,user_dict)
    db.flush()
    #role
    user_roles = [{"user_id": add_user.id, "role_id": i} for i in roleIds]
    db.bulk_insert_mappings(models.User_Role,user_roles)
    db.flush()
    return {
        "code": 20000,
        "data": "",
        "message": "新增成功",
    }

@router.put("/reset-password", response_model= schemas.Response)
def reset_password(
    db: Session = Depends(deps.get_db), user_id: int = Body(...),password: str = Body(...),User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Reset password
    """
    data = {
        "hashed_password":get_password_hash(password)
    }
    if User.is_superuser or User.id == user_id:
        db.query(models.User).filter(models.User.id == user_id).update(data)
        return { "code": 20000,"data": "","message": "修改成功",}
    else:
        return { "code": 40000,"data": "","message": "无修改权限",}

@router.delete("/{ids}", response_model=schemas.Response)
def delete_user(*, db: Session = Depends(deps.get_db), ids : str,
             current_user: models.User = Depends(deps.get_current_active_user)
             ) -> Any:
    ids = [int(id) for id in ids.split(",")]
    print(ids)
    db.query(models.User_Dict).filter(models.User_Dict.user_id.in_(ids)).delete(synchronize_session=False)
    db.query(models.User_Department).filter(models.User_Department.user_id.in_(ids)).delete(synchronize_session=False)
    db.query(models.User_Role).filter(models.User_Role.user_id.in_(ids)).delete(synchronize_session=False)
    db.query(models.User).filter(models.User.id.in_(ids)).delete(synchronize_session=False)
    return {
        "code": 20000,
        "data": "",
        "message": "新增成功",
    }
