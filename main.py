import discord

from src.settings.variables import *
from src.settings.configs import getIntents
from src.events import register_events
from src.settings.token import BOT_TOKEN
# Create a file token.py in src/settings and put the variable BOT_TOKEN="<token>"

def main():
	intents = getIntents()
	client = discord.Client(intents=intents)
	client.tree = discord.app_commands.CommandTree(client)
	register_events(client)
	client.run(BOT_TOKEN)

if __name__ == "__main__":
	main()
