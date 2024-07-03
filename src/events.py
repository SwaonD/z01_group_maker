from discord import Client, app_commands, Guild, Message, MessageType
from src.init import reload_groups
from src.commands import register_commands
from src.utils.log import LOGGER
from src.group.db_request.config import get_group_channel
from src.settings.variables import MSG, Variables as V
from src.welcome import send_welcome_message


def register_events(client: Client, tree: app_commands.CommandTree):
	@client.event
	async def on_ready():
		for guild in client.guilds:
			register_commands(tree, guild)
			await tree.sync(guild=guild)
			await reload_groups(guild)
			V.registered_guilds.add(guild.id)
		LOGGER.msg(f"{client.user} -- Ready Perfectly !")

	@client.event
	async def on_guild_join(guild: Guild):
		LOGGER.msg(f"I have joined {guild.name} ({guild.id})")
		if guild.id not in V.registered_guilds:
			register_commands(tree, guild)
			await tree.sync(guild=guild)
			V.registered_guilds.add(guild.id)
		await reload_groups(guild)
		await send_welcome_message(guild)

	@client.event
	async def on_message(message: Message):
		if message.author.bot or message.type != MessageType.default:
			return
		group_channel = await get_group_channel(message.guild)
		if group_channel is not None and message.channel.id == group_channel.id:
			await message.author.send(MSG.CHANNEL_COMMAND_ONLY % \
					(message.channel.jump_url), suppress_embeds=True)
			await message.delete()
