from discord import Client, app_commands

def register_events(client: Client, tree: app_commands.CommandTree):
	@client.event
	async def on_ready():
		for guild in client.guilds:
			await tree.sync(guild=guild)
		print(f"{client.user} est dans la place !")
