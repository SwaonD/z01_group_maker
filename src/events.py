from discord import Client

def register_events(client: Client, tree):
	@client.event
	async def on_ready():
		for guild in client.guilds:
			await tree.sync(guild=guild)
		print(f"{client.user} est dans la place !")
