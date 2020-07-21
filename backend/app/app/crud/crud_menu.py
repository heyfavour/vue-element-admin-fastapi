from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.role import Menu
from app.schemas.system.menu import MenuCreate, MenuUpdate


class CRUDMenu(CRUDBase[Menu, MenuCreate, MenuUpdate]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[Menu]:
        return db.query(Menu).filter(Menu.username == username).first()

    def create(self, db: Session, *, obj_in: MenuCreate) -> Menu:
        db_obj = Menu(
            username=obj_in.username,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Menu, obj_in: Union[MenuUpdate, Dict[str, Any]]
    ) -> Menu:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)




user = CRUDMenu(Menu)
