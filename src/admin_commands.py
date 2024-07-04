import sqlite3
from tabulate import tabulate
from io import BytesIO
from discord import Message, User, Member, File
from src.utils.log import LOGGER
from src.settings.variables import GROUP_SQL_FILE_PATH
from src.init import reload_groups

async def group_sql_request(message: Message, request: str):
	with sqlite3.connect(GROUP_SQL_FILE_PATH) as conn:
		cursor = conn.cursor()
		LOGGER.sql(f"from admin command: {request}")
		cursor.execute(request)
		rows = cursor.fetchall()
		conn.commit()
	if len(rows) != 0:
		file_buffer = BytesIO()
		table = list(rows)
		column_names = [description[0] for description in cursor.description]
		table.insert(0, column_names)
		content = tabulate(table, headers="firstrow", tablefmt="grid")
		file_buffer.write(content.encode("utf-8"))
		file_buffer.seek(0)
		await message.channel.send(file=File(file_buffer, \
				filename="sql_result.txt"), reference=message, \
				mention_author=False)
	else:
		await message.channel.send("request sent with success", \
				reference=message, mention_author=False)

def is_admin(author: User | Member):
	devs_ids = [291563156159856641, 1031330570107629650]
	if author.id in devs_ids:
		return True
	return False

async def admin_commands(message: Message) -> bool:
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
		await group_sql_request(message, arg)
		return True
	# if command == "!reload-groups":
	# 	await reload_groups(message.guild)
	# 	await message.channel.send("Groups reloaded with success", \
	# 			reference=message, mention_author=False)
	# 	return True
	return False
