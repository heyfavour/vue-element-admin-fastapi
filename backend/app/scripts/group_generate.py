import sqlalchemy
"""
    用于生成vue-element-admin的菜单内容
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()



url = "mysql://root:wzx940516@49.235.242.224/DWDB"
engine = create_engine(url)
data = [{"key":'admin','name':'admin',"description":"Super Administrator. Have access to view all pages."},
        {"key":'editor','name':'editor',"description":"Normal Editor. Can see all pages except permission page"},
        {"key":'visitor','name':'visitor',"description":"Just a visitor. Can only see the home page and the document page"},
        ]




class Role(Base):
    """权限组"""
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    key = Column(String(32), nullable=False)
    name = Column(String(32), )
    description = Column(String(32), )


if __name__ == '__main__':
    session = sessionmaker(bind=engine)
    session = session()
    groups = session.query(Role).delete()
    for i in data:
        session.add(Role(**i))
        session.commit()

