from discord import Client, app_commands, Message
from src.settings.variables import GROUP_CHANNEL_ID
from src.init import update_groups_from_db
from src.commands import register_commands

def register_events(client: Client, tree: app_commands.CommandTree):
	@client.event
	async def on_ready():
		register_commands(tree, client.guilds)
		for guild in client.guilds:
			await tree.sync(guild=guild)
			await update_groups_from_db(guild)
		print(f"{client.user} est dans la place !")

	# @client.event
	# async def on_message(message: Message):
	# 	if message.channel.id == GROUP_CHANNEL_ID and not message.author.bot:
	# 		await message.author.send(
	# 				"Seulement les commandes sont autorisées dans ce salon.")
	# 		await message.delete()
