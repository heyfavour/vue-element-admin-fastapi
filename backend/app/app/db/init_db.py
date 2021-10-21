import os, logging
import pandas as pd
import numpy as np
from app.db.session import engine,SessionLocal

logger = logging.getLogger(__name__)

def init_db() -> None:
    session = SessionLocal()
    # Tables should be created with Alembic migrations
    init_data_path = os.path.join(os.path.dirname(__file__), "init_data")
    files = ['department.csv', 'menu.csv', 'role.csv', 'user.csv', 'dict_type.csv', 'dict_data.csv',
             'role_menu.csv', 'user_department.csv', 'user_dict.csv', 'user_role.csv', ]
    for file in files:
        file_path = os.path.join(init_data_path, file)
        df = pd.read_csv(file_path, sep=",")
        if file == "menu.csv":
            df['component'] = df['component'].apply(lambda x: '' if pd.isnull(x) else x)
            df['name'] = df['name'].apply(lambda x: '' if pd.isnull(x) else x)
        logger.info(f"{file}  load successed")
        table_name = file.replace(".csv", "")
        df.to_sql(table_name, engine, if_exists="append", index=False)
        sql = f"ALTER TABLE {table_name} AUTO_INCREMENT = {max(df['id']) + 1}"
        session.execute(sql)
    session.commit()
    session.close()
