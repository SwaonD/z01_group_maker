from discord import Interaction, Embed, Colour, Intents
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.tools import is_project, project_exists
from src.group.message.tools import get_group_id
from src.utils.log import log
from src.group.message.view import GroupMessageView

def get_intents():
	# Cache
	intents = Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents
