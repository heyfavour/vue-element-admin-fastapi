from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session,joinedload_all
from app import models, schemas
from app.api import deps
from app.extensions.utils import tree_children


router = APIRouter()

@router.get("/list", response_model=schemas.Response)
def read_routes(db: Session = Depends(deps.get_db),
                current_user: models.User = Depends(deps.get_current_active_user)
                ) -> Any:
    """
    Retrieve Mock Data.
    """
    depts = db.query(models.Department
                     ).options(joinedload_all("children", "children", "children","children")
                               ).filter(models.Department.parent_id==None,models.Department.status==1).one()
    depts = [tree_children(depts),]
    return {
        "code": 20000,
        "data": depts,
        "message":"",
    }


@router.get("/{id}", response_model=schemas.Response)
def read_routes(*,db: Session = Depends(deps.get_db),
                id:int,
                current_user: models.User = Depends(deps.get_current_active_user)
                ) -> Any:
    dept = db.query(models.Department).filter(models.Department.id == id).one()

    return {
        "code": 20000,
        "data": dept,
        "message":"",
    }


def tree_children_exclude(node, id):
    if node.id == id:return {}
    if node.children == []:
        return node.dict()
    else:
        node_dict = node.dict()
        node_dict["children"] = [tree_children_exclude(child,id) for child in node.children]
    return node_dict

@router.get("/list/exclude/{id}", response_model=schemas.Response)
def read_routes(*,db: Session = Depends(deps.get_db),id:int,
                current_user: models.User = Depends(deps.get_current_active_user)
                ) -> Any:
    """
    Retrieve Mock Data.
    """
    depts = db.query(models.Department
                     ).options(joinedload_all("children", "children", "children","children")
                               ).filter(models.Department.parent_id==None,models.Department.status==1).one()
    depts = [tree_children_exclude(depts,id)]
    return {
        "code": 20000,
        "data": depts,
        "message":"",
    }


@router.put("/", response_model=schemas.Response)
def read_routes(*, db: Session = Depends(deps.get_db),data_in: schemas.DepartmentUpdate,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    db.query(models.Department).filter(models.Department.id == data_in.id).update(data_in)
    return {
        "code": 20000,
        "data": "",
        "message":"修改成功",
    }
