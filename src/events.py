from discord import Client
# from discord.ext import commands

def register_events(client: Client):
	@client.event
	async def on_ready():
		for guild in client.guilds:
			await client.tree.sync(guild=guild)
		print(f"{client.user} est dans la place !")
