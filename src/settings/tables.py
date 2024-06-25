from src.utils.sql import sql_create_table, \
	sql_insert_data, sql_get_data, sql_delete_data, sql_update_data
from src.settings.variables import GROUP_SQL_FILE, Group

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

	def delete_data(self, condition: str = ""):
		"""
		ex : table.delete_data(f"{table.message_id} = '{2}'")
		"""
		sql_delete_data(self.file, self.name, condition)

	def update_data(self, data: dict, condition: str):
		"""
		ex: table.update_data(f"{table.message_id} = {2}", newColumns)
		"""
		sql_update_data(self.file, self.name, data, condition)


class GroupsTable(BaseTable):
	def __init__(self):
		self.id = "id"
		self.message_id = "message_id"
		self.project_name = "project_name"
		self.leader_id = "leader_id"
		self.size_limit = "size_limit"
		self.description = "description"
		self.confirmed = "confirmed"
		columns = [
			f"{self.id} INTEGER PRIMARY KEY",
			f"{self.message_id} INTEGER",
			f"{self.project_name} STRING",
			f"{self.leader_id} INTEGER",
			f"{self.size_limit} INTEGER",
			f"{self.description} STRING",
			f"{self.confirmed} INTEGER"
		]
		super().__init__("groups", GROUP_SQL_FILE, columns)

	def insert_data(self, message_id: int, project_name: str, leader_id: int,
			size_limit: int, description: str,confirmed: int) -> int:
		data = {
			self.message_id: str(message_id),
			self.project_name: project_name,
			self.leader_id: str(leader_id),
			self.size_limit: str(size_limit),
			self.description: description,
			self.confirmed: str(confirmed)
		}
		return super().insert_data(data)

	def get_groups(self, condition: str = "") -> list[Group]:
		data = super().get_data(condition)
		result: list[Group] = []
		for row in data:
			group = Group(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
			result.append(group)
		return result

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
