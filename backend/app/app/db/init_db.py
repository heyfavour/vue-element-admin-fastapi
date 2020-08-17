from sqlalchemy.orm import Session

import os
from app import crud, schemas
from app.core.config import settings
from app.db.session import SessionLocal,engine
from app.db import base  # noqa: F401
import pandas as pd
# make sure all SQL Alchemy models are imported (app.db.modules) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    path = os.getcwd()
    if os.name in ('posix'):
        init_data_path = os.getcwd() + "/db/init_data"
    else:
        init_data_path = os.getcwd() + "\\db\\init_data"
    files = os.listdir(init_data_path)
    print(files)
    for file in files:
        print(file)
        if "csv" not in file:continue
        try:
            df  = pd.read_csv(init_data_path+"/"+file, sep=",")
        except:
            continue
        df.to_sql(file.replace(".csv",""),engine,if_exists="append",index=False)


