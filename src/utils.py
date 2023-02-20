import yaml
from sqlalchemy import create_engine

with open("config.yaml") as f:
    config=yaml.safe_load(f)

mysql_host=config["database"]["mysql"]["mysql_host"]
mysql_user=config["database"]["mysql"]["mysql_user"]
mysql_password=config["database"]["mysql"]["mysql_password"]
mysql_port=config["database"]["mysql"]["mysql_port"]
mysql_db_name=config["database"]["mysql"]["mysql_db_name"]

postgres_host=config["database"]["postgres"]["postgres_host"]
postgres_user=config["database"]["postgres"]["postgres_user"]
postgres_password=config["database"]["postgres"]["postgres_password"]
postgres_port=config["database"]["postgres"]["postgres_port"]
postgres_db_name=config["database"]["postgres"]["postgres_db_name"]

mysql_engine=create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db_name}',
 echo=True, connect_args={'auth_plugin': 'mysql_native_password'})
postgres_engine=create_engine(f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db_name}')
