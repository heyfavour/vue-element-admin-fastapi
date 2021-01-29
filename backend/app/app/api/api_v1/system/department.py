from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps
from app.extensions.utils import list_to_tree

router = APIRouter()


@router.get("/list", response_model=schemas.Response)
def get_departments(db: Session = Depends(deps.get_db), ) -> Any:
    """部门管理-查询"""
    departments = db.query(models.Department).all()
    departments = list_to_tree([department.dict() for department in departments])
    return {"code": 20000, "data": departments}


@router.post("/", response_model=schemas.Response)
def add_department(*, db: Session = Depends(deps.get_db), department: schemas.DepartmentCreate) -> Any:
    """部门管理-新增"""
    db.add(models.Department(**department.dict()))
    return {"code": 20000, "data": "", "message": "新增部门成功"}


@router.get("/{id}", response_model=schemas.Response)
def get_department(*, db: Session = Depends(deps.get_db), id: int, ) -> Any:
    """部门管理-更新前查询"""
    department = db.query(models.Department).filter(models.Department.id == id).one()
    return {"code": 20000, "data": department, }


@router.get("/list/exclude/{id}", response_model=schemas.Response)
def get_department_exclude_id(*, db: Session = Depends(deps.get_db), id: int, ) -> Any:
    """返回一个排除了子节点的树结构"""
    departments = db.query(models.Department).all()
    departments = list_to_tree([department.dict() for department in departments], order="order", exclude=id)
    return {"code": 20000, "data": departments, }


@router.put("/", response_model=schemas.Response)
def update_department(*, db: Session = Depends(deps.get_db), department: schemas.DepartmentUpdate) -> Any:
    """部门管理-修改"""
    db.query(models.Department).filter(models.Department.id == department.id).update(department)
    return {"code": 20000, "message": "修改成功", }


@router.delete("/{department_id}", response_model=schemas.Response)
def delete_department_id(department_id: int, db: Session = Depends(deps.get_db), ) -> Any:
    """部门管理-删除"""
    users = db.query(models.User_Department).filter(models.User_Department.department_id == department_id).all()
    if users != []: raise HTTPException(status_code=200, detail="该部门下存在员工，禁止删除")
    db.query(models.Department).filter(models.Department.id == department_id).delete()
    return {"code": 20000, "message": f"删除成功"}
