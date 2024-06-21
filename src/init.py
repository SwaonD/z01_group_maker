from discord import Intents
from src.settings.tables import GroupTable

def getIntents():
	# Cache
	intents = Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents
