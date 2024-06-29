from discord import Client, app_commands, Guild, Message
from src.init import reload_groups
from src.commands import register_commands
from src.utils.log import LOGGER
from src.group.db_request.config import get_group_channel
from src.settings.variables import MSG

def register_events(client: Client, tree: app_commands.CommandTree):
	@client.event
	async def on_ready():
		register_commands(tree, client.guilds)
		for guild in client.guilds:
			await tree.sync(guild=guild)
			await reload_groups(guild)
		LOGGER.msg(f"{client.user} - Ready Perfectly !")

	@client.event
	async def on_guild_join(guild: Guild):
		LOGGER.msg(f"I have joined {guild.name} ({guild.id})")
		register_commands(tree, client.guilds)
		await tree.sync(guild=guild)
		await reload_groups(guild)

	@client.event
	async def on_message(message: Message):
		if message.author.bot:
			return
		group_channel = await get_group_channel(message.guild)
		if group_channel is not None and message.channel.id == group_channel.id:
			await message.author.send(
					MSG.CHANNEL_COMMAND_ONLY % (message.channel.jump_url))
			await message.delete()
