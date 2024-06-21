import sqlite3
from src.settings.variables import DATA_SQL_FILE

async def sql_add_group(message_id, project_name, creator_id):
	print("add group in db")
	conn = sqlite3.connect(DATA_SQL_FILE)
	cursor = conn.cursor()
	cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
	id INTEGER PRIMARY KEY,
	message_id INTEGER,
	project_name STRING,
	creator_id INTEGER
)
''')
	cursor.execute('''
	INSERT INTO groups (message_id, project_name, creator_id) VALUES (?, ?, ?)
''', (message_id, project_name, creator_id))
	conn.commit()
	conn.close()
