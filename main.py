from discord import Client, app_commands
from src.settings.variables import Variables as V
from src.init import get_intents, init
from src.events import register_events

def main():
	init()
	intents = get_intents()
	client = Client(intents=intents)
	tree = app_commands.CommandTree(client)
	register_events(client, tree)
	if not V.BOT_TOKEN:
		raise ValueError("No discord bot token provided.")
	client.run(V.BOT_TOKEN)

if __name__ == "__main__":
	main()
