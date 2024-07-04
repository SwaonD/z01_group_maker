import sqlite3
from src.utils.log import LOGGER

def sql_escape(s: str):
	return s.replace("'", "''")

def sql_create_table(file: str, name: str, *columns: str):
	variables = ""
	request = ""
	for i, elem in enumerate(columns):
		variables += elem
		if i != len(columns)-1:
			variables += ", "
	request = f"CREATE TABLE IF NOT EXISTS {name} ({variables})"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		LOGGER.sql(request)
		cursor.execute(request)
		conn.commit()

def sql_get_data(file: str,
		table_name: str, condition: str = "", *columns: str) -> list[tuple]:
	columns_str = ""
	request = ""
	for i, col in enumerate(columns):
		columns_str += col
		if i != len(columns)-1:
			columns_str += ", "
	if columns_str == "":
		columns_str = "*"
	request = f"SELECT {columns_str} FROM {table_name}"
	if condition != "":
		request += f" WHERE {condition}"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		LOGGER.sql(request)
		cursor.execute(request)
		rows = cursor.fetchall()
		conn.commit()
		return rows

def sql_insert_data(file: str, table_name: str, data: dict[str:str]) -> int:
	"""
	returns INTEGER PRIMARY KEY if it exists
	"""
	keys_str = ", ".join(data.keys())
	values_str = [f"'{sql_escape(value)}'" for value in data.values()]
	values_str = ", ".join(values_str)
	request = f"INSERT INTO {table_name} ({keys_str}) VALUES ({values_str})"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		LOGGER.sql(request)
		cursor.execute(request)
		conn.commit()
		return cursor.lastrowid
# INSERT INTO groups (guild_id, channel_id, message_id, project_name, leader_id, size_limit, description, confirmed) VALUES (', [, ', 3, 5, 2, 5, 0, 9, 3, 7, 5, 2, 6, 6, 4, 2, 2, 7, 9, 7, ', ,,  , ', 1, 2, 5, 3, 7, 1, 9, 7, 5, 1, 5, 4, 1, 2, 6, 4, 4, 3, 4, ', ,,  , ', 1, 2, 5, 8, 4, 3, 3, 4, 6, 0, 9, 8, 5, 5, 2, 8, 4, 2, 1, ', ,,  , ', a, s, c, i, i, -, a, r, t, -, w, e, b, -, s, t, y, l, i, z, e, ', ,,  , ', 2, 9, 1, 5, 6, 3, 1, 5, 6, 1, 5, 9, 8, 5, 6, 6, 4, 1, ', ,,  , ', 2, ', ,,  , ", I, N, S, E, R, T,  , I, N, T, O,  , g, r, o, u, p, _, m, e, m, b, e, r, s,  , (, g, r, o, u, p, _, i, d, ,,  , u, s, e, r, _, i, d, ),  , V, A, L, U, E, S,  , (, ', ', 2, ', ', ,,  , ', ', 1, 0, 3, 1, 3, 3, 0, 5, 7, 0, 1, 0, 7, 6, 2, 9, 6, 5, 0, ', ', ), ", ,,  , ', 0, ', ], ')


def sql_delete_data(file: str, table_name: str, condition: str = ""):
	request = f"DELETE FROM {table_name}"
	if condition != "":
		request += f" WHERE {condition}"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		LOGGER.sql(request)
		cursor.execute(request)
		conn.commit()

def sql_update_data(file: str, table_name: str, data: dict[str:str], condition: str):
	d = ""
	for i, (key, values) in enumerate(data.items()):
		d += f"{key} = {values}"
		if i != len(data.keys())-1:
			d += ","

	request = f"UPDATE {table_name} SET {d} WHERE {condition}"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		LOGGER.sql(request)
		cursor.execute(request)
		conn.commit()
