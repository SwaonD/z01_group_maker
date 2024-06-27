import os
from discord import Client, app_commands
from src.settings.variables import *
from src.init import get_intents, init
from src.events import register_events

def main():
	init()
	intents = get_intents()
	client = Client(intents=intents)
	tree = app_commands.CommandTree(client)
	register_events(client, tree)
	bot_token = os.getenv("Z_01_GROUP_MAKER_DISCORD_BOT_TOKEN")
	if not bot_token:
		raise ValueError("No discord bot token provided.")
	client.run(bot_token)

if __name__ == "__main__":
	main()
