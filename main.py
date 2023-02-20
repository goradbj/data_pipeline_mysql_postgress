from src.pipeline import *

def main():
    mysql_df=read_mysql_data()
    mysql_df=transform_mysql_data(mysql_df)
    write_data(mysql_df)

if __name__=="__main__":
    main()