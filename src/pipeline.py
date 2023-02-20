import pandas as pd
from src.utils import *

# read data from mysql
def read_mysql_data():
    mysql_query = "SELECT id, name, email FROM users"
    mysql_df = pd.read_sql_query(mysql_query, mysql_engine)
    print("Data read from MySQL Database")
    print("No of Records Found in MySQL:", mysql_df.shape[0])
    return mysql_df

# transform data
def transform_mysql_data(mysql_df):
    mysql_df = mysql_df.rename(columns={'id': 'user_id', 'name': 'full_name'})
    mysql_df['user_id'] = mysql_df['user_id'].astype(str)
    print("Data tranformation done")
    return mysql_df

# Save data to Postgress
def write_data(mysql_df):
    postgres_table = 'users'
    mysql_df.to_sql(postgres_table, postgres_engine, if_exists='replace', index=False)
    print("No of Records stored in Postgres:", mysql_df.shape[0])
    print("Data stored to Postgres Database")

