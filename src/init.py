from discord import Intents

def get_intents():
	# Cache
	intents = Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents
