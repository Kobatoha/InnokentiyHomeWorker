import duckdb


database = 'lowadi/DataBase/lowadi.duckdb'


def create_connection(db_file=database):
    connect = duckdb.connect(database=database)
    return connect