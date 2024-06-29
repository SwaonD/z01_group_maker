from discord import Client, app_commands, Guild
from src.init import update_groups_from_db
from src.commands import register_commands
from src.utils.log import LOGGER

def register_events(client: Client, tree: app_commands.CommandTree):
	@client.event
	async def on_ready():
		register_commands(tree, client.guilds)
		for guild in client.guilds:
			await tree.sync(guild=guild)
			await update_groups_from_db(guild)
		LOGGER.msg(f"{client.user} - Ready Perfectly !")

	@client.event
	async def on_guild_join(guild: Guild):
		LOGGER.msg(f"I have joined {guild.name} ({guild.id})")
		register_commands(tree, client.guilds)
		await tree.sync(guild=guild)
		await update_groups_from_db(guild)

	# @client.event
	# async def on_message(message: Message):
	# 	if message.channel.id == GROUP_CHANNEL_ID and not message.author.bot:
	# 		await message.author.send(
	# 				"Seulement les commandes sont autorisées dans ce salon.")
	# 		await message.delete()
