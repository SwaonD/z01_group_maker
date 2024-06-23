import sqlite3
from src.utils.log import log


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
		log(request, True)
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
		log(request, True)
		cursor.execute(request)
		rows = cursor.fetchall()
		conn.commit()
		return rows


def sql_insert_data(file: str, table_name: str, data: dict[str:str]) -> int:
	"""
	returns INTEGER PRIMARY KEY if it exists
	"""
	keys_str = ""
	values_str = ""
	request = ""
	for i, (key, values) in enumerate(data.items()):
		keys_str += key
		values_str += f"'{values}'"
		if i != len(data.keys())-1:
			keys_str += ", "
			values_str += ", "
	request = f"INSERT INTO {table_name} ({keys_str}) VALUES ({values_str})"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		log(request, True)
		cursor.execute(request)
		conn.commit()
		return cursor.lastrowid


def sql_delete_data(file: str, table_name: str, condition: str = ""):
	request = f"DELETE FROM {table_name}"
	if condition != "":
		request += f" WHERE {condition}"
	with sqlite3.connect(file) as conn:
		cursor = conn.cursor()
		log(request, True)
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
		log(request, True)
		cursor.execute(request)
		conn.commit()
