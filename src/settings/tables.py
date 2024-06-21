from src.utils.sql import sql_create_table, sql_insert_data as sql_insert_data
from src.settings.variables import DATA_SQL_FILE


class GroupTable():
	def __init__(self):
		self.name = "groups"
		self.message_id_str = "message_id"
		self.project_name_str = "project_name"
		self.creator_id_str = "creator_id"
		sql_create_table(DATA_SQL_FILE, self.name, True,
				f"{self.message_id_str} INTEGER",
				f"{self.project_name_str} STRING",
				f"{self.creator_id_str} INTEGER")
	def insert_data(self, message_id:int, project_name:str, creator_id:int):
		sql_insert_data(DATA_SQL_FILE, self.name, {
			self.message_id_str: str(message_id),
			self.project_name_str: project_name,
			self.creator_id_str: str(creator_id)
		})

GROUP_TABLE = GroupTable()
