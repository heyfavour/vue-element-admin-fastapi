from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException,Body,Request
from sqlalchemy.orm import Session,joinedload_all,contains_eager,Load
from fastapi.encoders import jsonable_encoder
from app import models, schemas
from app.api import deps


router = APIRouter()

@router.get("/type/list", response_model=schemas.Response)
def read_routes(db: Session = Depends(deps.get_db),
                page: Optional[int] = 0,
                limit: Optional[int] = 10,
                current_user: models.User = Depends(deps.get_current_active_user)
                ) -> Any:
    """
    Retrieve Mock Data.
    """
    query = db.query(models.Dict_Type)
    total = query.count()
    items = query.limit(limit).offset((page-1)*limit).all()
    return {
        "code": 20000,
        "data": {
            "items": items,
            'total':  total
        },
        "message":"",
    }


@router.get("/type/all", response_model=schemas.Response)
def read_routes(db: Session = Depends(deps.get_db),current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    字典数据 查询所有字典
    """
    types = db.query(models.Dict_Type).all()
    return {"code": 20000,"data": types,"message":"",}


@router.get("/type/{id}", response_model=schemas.Response)
def read_routes(*, db: Session = Depends(deps.get_db),id: int,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    type = db.query(models.Dict_Type).filter(models.Dict_Type.id == id).one()
    return {
        "code": 20000,
        "data": type,
        "message":"",
    }

@router.put("/type", response_model=schemas.Response)
def read_routes(*, db: Session = Depends(deps.get_db),type_in: schemas.DictTypeUpdate,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    db.query(models.Dict_Type).filter(models.Dict_Type.id == type_in.id).update(type_in)
    db.commit()
    return {
        "code": 20000,
        "data": "",
        "message":"修改成功",
    }

@router.post("/type", response_model=schemas.Response)
def read_routes(*,db: Session = Depends(deps.get_db),type_in: schemas.DictTypeCreate,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    字典TYPE 新增
    """
    rows = db.add(models.Dict_Type(**jsonable_encoder(type_in)))
    db.commit()
    return {
        "code": 20000,
        "data": "",
        "message":"新增成功",
    }


@router.get("/data/list", response_model=schemas.Response)
def read_routes(*,db: Session = Depends(deps.get_db),
                type_id:str,
                page: int = 0,
                limit: int = 100,
                current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Retrieve Mock Data.
    """
    query = db.query(models.Dict_Data).join(models.Dict_Type, models.Dict_Type.id == models.Dict_Data.type_id
                                           ).filter(models.Dict_Type.id == type_id)
    total = query.count()
    items = query.limit(limit).offset((page-1)*limit).all()
    print(items)
    return {
        "code": 20000,
        "data": {
            "items": items,
            'total':  total
        },
        "message":"修改成功",
    }

@router.get("/data/{id}", response_model=schemas.Response)
def read_routes(*, db: Session = Depends(deps.get_db),id: int,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    data = db.query(models.Dict_Data).filter(models.Dict_Data.id == id).one()
    return {
        "code": 20000,
        "data": data,
        "message":"",
    }

@router.put("/data/", response_model=schemas.Response)
def read_routes(*, db: Session = Depends(deps.get_db),data_in: schemas.DictDataUpdate,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    db.query(models.Dict_Data).filter(models.Dict_Data.id == data_in.id).update(data_in)
    db.commit()
    return {
        "code": 20000,
        "data": "",
        "message":"修改成功",
    }

@router.post("/data/", response_model=schemas.Response)
def read_routes(*, db: Session = Depends(deps.get_db),data_in: schemas.DictDataCreate,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    db.add(models.Dict_Data(**jsonable_encoder(data_in)))
    db.commit()
    return {
        "code": 20000,
        "data": "",
        "message":"修改成功",
    }


@router.get("/data/type/{type_code}", response_model=schemas.Response)
def get_data_type_code(*, db: Session = Depends(deps.get_db),type_code:str,current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    data = db.query(models.Dict_Type).filter(models.Dict_Type.code == type_code).one().data
    data  = [{"id":i.id,"label":i.label} for i in data]
    return {
        "code": 20000,
        "data": data,
        # "message":"修改成功",
    }



