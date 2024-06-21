import discord

import os
from dotenv import load_dotenv
from src.settings.variables import *
from src.settings.configs import getIntents
from src.events import register_events

load_dotenv()

def main():
	intents = getIntents()
	client = discord.Client(intents=intents)
	client.tree = discord.app_commands.CommandTree(client)
	register_events(client)

	bot_token = os.getenv("Z_01_GROUP_MAKER_DISCORD_BOT_TOKEN")
	if not bot_token:
		raise ValueError("No discord bot token provided.")
	client.run(bot_token)

if __name__ == "__main__":
	main()
