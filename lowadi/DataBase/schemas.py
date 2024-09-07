from .connect_duckdb import create_connection

"""
tables:
pufo - url varchar, ufo varchar
"""


def create_table(table_name: str, data: dict) -> None:
    con = create_connection()

    con.close()


def insert_data(datas: list[list]) -> None:
    con = create_connection()
    for data in datas:
        con.sql(f"INSERT INTO pufo VALUES ('{data[0]}', '{data[1]}')")
        print(f"Добавлено в таблицу pufo. Пользователь: {data[0]}, НЛО: {data[1]}")


