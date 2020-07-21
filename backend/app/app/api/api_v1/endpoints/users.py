from typing import Any, List, Dict

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.utils import verify_password_reset_token
from app.core.security import get_password_hash


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

