import pandas as pd
import os
from app.db.session import SessionLocal,engine
db = SessionLocal()
sql = """
    SELECT TABLE_NAME FROM information_schema.`TABLES` WHERE TABLE_SCHEMA = 'DWDB' AND TABLE_NAME != 'alembic_version'
"""
rows = db.execute(sql).fetchall()
for table in rows:
    table_name = table[0]
    sql  = f"""
    SELECT * FROM DWDB.{table_name }
    """

    df = pd.read_sql(sql,con=engine)
    file_path = os.path.join(os.path.dirname(__file__) ,"init_data",f"{table_name}.csv")
    print(file_path)
    df.to_csv(file_path,index=0)
