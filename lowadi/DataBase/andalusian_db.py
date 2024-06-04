import duckdb


def create_connection(db_file):
    connect = duckdb.connect(database=db_file)
    return connect


def create_table(connect):
    create_table_duck = """
    CREATE TABLE IF NOT EXISTS andalusian (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        birthday DATE,
        sex TINYINT,
        color VARCHAR,
        rare TINYINT,
        armor BOOLEAN,
        speed BOOLEAN,
        dressage BOOLEAN,
        galop BOOLEAN,
        forest BOOLEAN,
        montains BOOLEAN
    );
    """
    conn.execute(create_table_duck)

# Подключаемся к базе данных и создаем таблицу
db_file = 'example.duckdb'
conn = create_connection(db_file)
create_table(conn)
conn.close()
