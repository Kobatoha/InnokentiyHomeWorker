import duckdb


database = 'lowadi/DataBase/lowadi.duckdb'


def create_connection(db_file='lowadi/DataBase/' + database):
    connect = duckdb.connect(database=database)
    return connect