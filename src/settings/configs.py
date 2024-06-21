import discord

def getIntents():
	# Cache
	intents = discord.Intents.default()
	intents.message_content = True
	intents.members = True
	intents.guilds = True
	return intents
