import os, logging
import pandas as pd

from app.db.session import engine

logger = logging.getLogger(__name__)


def init_db() -> None:
    # Tables should be created with Alembic migrations
    init_data_path = os.path.join(os.getcwd(), "db", "init_data")
    files = ['department.csv', 'menu.csv', 'role.csv', 'user.csv', 'dict_type.csv', 'dict_data.csv',
             'role_menu.csv', 'user_department.csv', 'user_dict.csv', 'user_role.csv', ]
    for file in files:
        file_path = os.path.join(init_data_path, file)
        df = pd.read_csv(file_path, sep=",")
        logger.info(f"{file}  load successed")
        df.to_sql(file.replace(".csv", ""), engine, if_exists="append", index=False)
