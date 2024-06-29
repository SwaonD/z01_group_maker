from discord import Intents, Guild
from discord.errors import NotFound
from src.group.message.view import GroupMessageView
from src.settings.tables import GROUPS_TABLE, GROUP_MEMBERS_TABLE, GROUPS_CONFIG
from src.settings.variables import Group, GROUP_SQL_FILE_PATH, \
		MSG_LOG_FILE_PATH, SQL_LOG_FILE_PATH, GENERAL_LOG_FILE_PATH
from src.utils.log import LOGGER
from pathlib import Path

def get_intents():
	# Cache
	intents = Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents

def create_files():
	file_paths = [Path(GROUP_SQL_FILE_PATH), Path(MSG_LOG_FILE_PATH),
			Path(SQL_LOG_FILE_PATH), Path(GENERAL_LOG_FILE_PATH)]
	for path in file_paths:
		if not path.parent.exists():
			path.parent.mkdir(parents=True, exist_ok=True)
		if not path.exists():
			path.touch()

def init():
	create_files()
	GROUPS_CONFIG.init_table()
	GROUPS_TABLE.init_table()
	GROUP_MEMBERS_TABLE.init_table()

async def update_groups_from_db(guild: Guild):
	groups: list[Group] = GROUPS_TABLE.get_groups()
	for group in groups:
		try:
			channel = guild.get_channel(group.channel_id)
			if channel is None:
				channel = await guild.fetch_channel(group.channel_id)
			message = await channel.fetch_message(group.message_id)
			# partial message from cache don't know if the message still exists
		except NotFound:
			GROUP_MEMBERS_TABLE.delete_data(
					f"{GROUP_MEMBERS_TABLE.group_id} = {group.id}")
			GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {group.id}")
			LOGGER.msg(f"Message for group number {group.id} ({group.project_name})" \
					+ " not found, data removed from db")
			continue
		view = GroupMessageView()
		await message.edit(view=view)
		LOGGER.msg(f"update: {group.project_name}. channel_id={group.channel_id}" \
				+ f" message_id={group.message_id}")
