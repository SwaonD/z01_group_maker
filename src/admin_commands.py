import sqlite3
from tabulate import tabulate
from io import BytesIO
from discord import Message, User, Member, File, Embed, Client
from src.utils.log import LOGGER
from src.settings.variables import GROUP_SQL_FILE_PATH, DEVS_IDS_STR
from src.init import reload_groups
from src.welcome import send_welcome_message

ADMIN_CMD_SQL_REQUEST = "sql-request"
ADMIN_CMD_SQL_REQUEST_ALT = "sql"
ADMIN_CMD_RELOAD_GROUPS = "reload-groups"
ADMIN_CMD_SEND_WELCOME_MSG = "send-welcome-msg"
ADMIN_CMD_HELP = "help"

async def _print_help_message(message: Message):
	help_embed = Embed()
	help_embed.add_field(
			name=ADMIN_CMD_SQL_REQUEST + "  |  " + ADMIN_CMD_SQL_REQUEST_ALT,
			value="make a request to the group db", inline=False)
	help_embed.add_field(
			name=ADMIN_CMD_RELOAD_GROUPS,
			value="reload every groups of the guild", inline=False)
	help_embed.add_field(
			name=ADMIN_CMD_SEND_WELCOME_MSG,
			value="send welcome message in the current channel", inline=False)
	help_embed.add_field(
			name=ADMIN_CMD_HELP,
			value="print this help message", inline=False)
	await message.channel.send(
			embed=help_embed, reference=message, mention_author=False)

async def _group_sql_request(message: Message, request: str):
	if len(request) == 0:
		return
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

async def _force_reload_groups(message: Message):
	if message.guild is not None:
		await reload_groups(message.guild)
		await message.channel.send("Groups reloaded with success", \
				reference=message, mention_author=False)
	else:
		await message.channel.send("Reload groups failed, no guild found", \
				reference=message, mention_author=False)

def _is_admin(author: User | Member):
	if DEVS_IDS_STR is not None:
		devs_ids = [int(x) for x in DEVS_IDS_STR.split(',')]
	else:
		devs_ids = []
	if author.id in devs_ids:
		return True
	return False

async def admin_commands(client: Client, message: Message) -> bool:
	"""
	return whether the message is an admin command
	"""
	if not message.content or not _is_admin(message.author):
		return False
	parts = message.content.split(None, 2)
	mention = parts[0] if parts else ""
	if mention != client.user.mention:
		return False
	cmd = parts[1] if len(parts) > 1 else ""
	arg = parts[2] if len(parts) > 2 else ""
	if cmd == ADMIN_CMD_HELP:
		await _print_help_message(message)
		return True
	if cmd == ADMIN_CMD_SQL_REQUEST or cmd == ADMIN_CMD_SQL_REQUEST_ALT:
		await _group_sql_request(message, arg)
		return True
	if cmd == ADMIN_CMD_RELOAD_GROUPS:
		await _force_reload_groups(message)
		return True
	if cmd == ADMIN_CMD_SEND_WELCOME_MSG:
		await send_welcome_message(message.guild, message.channel)
		return True
	return False
