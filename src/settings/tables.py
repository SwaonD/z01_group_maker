from src.utils.sql import sql_create_table, sql_insert_data, sql_get_data
from src.settings.variables import DATA_SQL_FILE


class GroupTable():
	def __init__(self):
		self.name = "groups"
		self.id = "id"
		self.message_id = "message_id"
		self.project_name = "project_name"
		self.creator_id = "creator_id"
		sql_create_table(DATA_SQL_FILE, self.name,
				f"{self.id} INTEGER PRIMARY KEY",
				f"{self.message_id} INTEGER",
				f"{self.project_name} STRING",
				f"{self.creator_id} INTEGER")
	def insert_data(self, message_id:int, project_name:str, creator_id:int):
		sql_insert_data(DATA_SQL_FILE, self.name, {
			self.message_id: str(message_id),
			self.project_name: project_name,
			self.creator_id: str(creator_id)
		})
	def get_data(self, condition:str="", *columns:str) -> list[tuple]:
		"""
		ex : table.get_data(f"{table.message_id} = 2", table.id)\n
		default * if no columns
		"""
		return sql_get_data(DATA_SQL_FILE, self.name, condition, *columns)
	# delete data
GROUP_TABLE = GroupTable()
