import sqlite3
from discord import Message, User, Member
from src.utils.log import LOGGER
from src.settings.variables import GROUP_SQL_FILE_PATH

def group_sql_request(request: str):
	with sqlite3.connect(GROUP_SQL_FILE_PATH) as conn:
		cursor = conn.cursor()
		LOGGER.sql(request)
		cursor.execute(request)
		conn.commit()

def is_admin(author: User | Member):
	if author.guild_permissions.administrator:
		return True
	return False

def admin_commands(message: Message) -> bool:
	"""
	return whether the message is an admin command
	"""
	content = message.content.strip()
	if not content or not is_admin(message.author):
		return False
	parts = content.split(" ", 1)
	command = parts[0] if parts else ""
	arg = parts[1] if len(parts) > 1 else ""
	if command == "!group-sql-request":
		group_sql_request(arg)
		return True
	return False
