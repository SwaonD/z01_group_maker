from discord import Intents
from src.settings.tables import GroupsTable

def getIntents():
	# Cache
	intents = Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents
