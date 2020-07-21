from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/list", response_model=schemas.Response)
def transaction(db: Session = Depends(deps.get_db),current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Retrieve Mock Data.
    """
    import random
    return {
        "code": 20000,
        "data": {
            "total": 20,
            'items':  [{"order_no": 1000+i,"price": random.randint(100,500),'status':random.choice(['success', 'pending'])} for i in range(20)]
        },
        "message":"",
    }

