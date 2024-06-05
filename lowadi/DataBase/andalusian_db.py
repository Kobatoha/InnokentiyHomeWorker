import duckdb


def create_connection(db_file):
    connect = duckdb.connect(database=database)
    return connect


def create_table(connect):
    create_table_duck = """
    CREATE TABLE IF NOT EXISTS andalusian (
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
        montains BOOLEAN,
        url VARCHAR
    );
    """
    conn.execute(create_table_duck)


def insert_table(connect, data: list) -> None:
    query = f"""
    INSERT INTO andalusian 
    (name, birthday, sex, color, rare, armor, speed, dressage, galop, forest, montains, url) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    connect.execute(query, data)
    connect.commit()
    print(f'INSERT: {data[0]} in andalusian team')


def view_table(connect):
    result = connect.execute('select * from andalusian').fetchall()
    return result


database = r'C:\Users\Admin\Desktop\python\Innokentiy\lowadi\DataBase\andalusian.duckdb'

if __name__ == '__main__':

    conn = create_connection(database)
    create_table(conn)
    conn.close()
