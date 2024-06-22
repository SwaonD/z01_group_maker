from src.utils.sql import sql_create_table, \
	sql_insert_data, sql_get_data, sql_delete_data
from src.settings.variables import GROUP_SQL_FILE

class BaseTable():
	def __init__(self, table_name: str, db_file: str, columns: list[str]):
		self.name = table_name
		self.file = db_file
		sql_create_table(self.file, self.name, *columns)

	def insert_data(self, data: dict) -> int:
		return sql_insert_data(self.file, self.name, data)

	def get_data(self, condition: str = "", *columns: str) -> list[tuple]:
		"""
		ex : table.get_data(f"{table.message_id} = '{2}'", table.id)\n
		default * if no columns
		"""
		return sql_get_data(self.file, self.name, condition, *columns)

	def delete_data(self, condition: str=""):
		"""
		ex : table.delete_data(f"{table.message_id} = '{2}'")
		"""
		sql_delete_data(self.file, self.name, condition)

class GroupsTable(BaseTable):
	def __init__(self):
		self.id = "id"
		self.message_id = "message_id"
		self.project_name = "project_name"
		self.creator_id = "creator_id"
		columns = [
			f"{self.id} INTEGER PRIMARY KEY",
			f"{self.message_id} INTEGER",
			f"{self.project_name} STRING",
			f"{self.creator_id} INTEGER"
		]
		super().__init__("groups", GROUP_SQL_FILE, columns)

	def insert_data(self,
			message_id: int, project_name: str, creator_id: int) -> int:
		data = {
			self.message_id: str(message_id),
			self.project_name: project_name,
			self.creator_id: str(creator_id)
		}
		return super().insert_data(data)

class GroupMembersTable(BaseTable):
	def __init__(self):
		self.id = "id"
		self.group_id = "group_id"
		self.user_id = "user_id"
		columns = [
			f"{self.id} INTEGER PRIMARY KEY",
			f"{self.group_id} INTEGER",
			f"{self.user_id} INTEGER"
		]
		super().__init__("group_members", GROUP_SQL_FILE, columns)

	def insert_data(self, group_id: int, user_id: int):
		data = {
			self.group_id: group_id,
   			self.user_id: user_id
		}
		super().insert_data(data)
  

GROUPS_TABLE = GroupsTable()
GROUP_MEMBERS_TABLE = GroupMembersTable()
