import sqlite3

def sql_insert_data(file:str, table_name:str, data:dict[str:str]):
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	keys_str = ""
	values_str = ""
	for i, (key, values) in enumerate(data.items()):
		keys_str += key
		values_str += f"'{values}'"
		if i != len(data.keys())-1:
			keys_str += ", "
			values_str += ", "
	print(f"INSERT INTO {table_name} ({keys_str}) VALUES ({values_str})")
	cursor.execute(f"INSERT INTO {table_name} ({keys_str}) VALUES ({values_str})")
	conn.commit()
	conn.close()

def sql_create_table(file:str, name:str, has_primary_id:bool, *columns:str):
	conn = sqlite3.connect(file)
	cursor = conn.cursor()
	variables = ""
	if has_primary_id:
		variables += "id INTEGER PRIMARY KEY"
		if len(columns) != 0:
			variables += ", "
	for i, elem in enumerate(columns):
		variables += elem
		if i != len(columns)-1:
			variables += ", "
	cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({variables})")
	conn.commit()
	conn.close()
