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
    insert into andalusian 
    (name, birthday, sex, color, rare, armor, speed, dressage, galop, forest, montains, url) 
    values 
    ('{data[0]}', '{data[1]}', {data[2]}, '{data[3]}', {data[4]}, {data[5]}, {data[6]}, {data[7]}, {data[8]}, {data[9]}, 
    {data[10]}, '{data[11]}')
    """
    connect.execute(query)
    connect.commit()
    print(f'INSERT: {data[0]} in andalusian team')


database = r'C:\Users\Admin\Desktop\python\Innokentiy\lowadi\DataBase\andalusian.duckdb'

if __name__ == '__main__':

    conn = create_connection(database)
    create_table(conn)
    conn.close()
