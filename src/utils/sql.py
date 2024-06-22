import sqlite3

def sql_get_data(file:str,
		table_name:str, condition:str="", *columns:str) -> list[tuple]:
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	columns_str = ""
	request = ""
	for i, col in enumerate(columns):
		print(f"col = {col}")
		columns_str += col
		if i != len(columns)-1:
			columns_str += ", "
	if columns_str == "":
		columns_str = "*"
	request = f"SELECT {columns_str} FROM {table_name}"
	if condition != "":
		request += f" WHERE {condition}"
	print(request)
	cursor.execute(request)
	rows = cursor.fetchall()
	conn.commit()
	conn.close()
	return rows

def sql_insert_data(file:str, table_name:str, data:dict[str:str]):
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
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
	print(request)
	cursor.execute(request)
	conn.commit()
	conn.close()

def sql_create_table(file:str, name:str, *columns:str):
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	variables = ""
	for i, elem in enumerate(columns):
		variables += elem
		if i != len(columns)-1:
			variables += ", "
	cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({variables})")
	conn.commit()
	conn.close()
