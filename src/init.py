from discord import Intents, Client
from src.group.message.view import GroupMessageView
from src.settings.tables import GROUPS_TABLE
from src.settings.variables import Group, GROUP_CHANNEL_ID, \
		MSG_LOG_FILE_PATH, SQL_LOG_FILE_PATH, GENERAL_LOG_FILE_PATH
from src.utils.log import log
from pathlib import Path

def get_intents():
	# Cache
	intents = Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents

def create_log_files():
	file_paths = [Path(MSG_LOG_FILE_PATH),
			Path(SQL_LOG_FILE_PATH), Path(GENERAL_LOG_FILE_PATH)]
	for path in file_paths:
		if not path.exists():
			path.touch()

def init():
	create_log_files()

async def update_groups_from_db(client: Client):
	groups: list[Group] = GROUPS_TABLE.get_groups()
	group_channel = client.get_channel(GROUP_CHANNEL_ID)
	if group_channel is None:
		group_channel = client.fetch_channel(GROUP_CHANNEL_ID)
	for group in groups:
		message = group_channel.get_partial_message(group.message_id)
		if message is None:
			message = await group_channel.fetch_message(group.message_id)
		view = GroupMessageView()
		await message.edit(view=view)
		log("update : " + group.project_name, MSG_LOG_FILE_PATH)
