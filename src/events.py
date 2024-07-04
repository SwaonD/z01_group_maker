from discord import Client, app_commands, Guild, Message, MessageType, errors
from src.init import reload_groups
from src.commands import register_commands
from src.utils.log import LOGGER
from src.group.db_request.config import get_group_channel
from src.settings.variables import MSG, Variables as V
from src.welcome import send_welcome_message
from src.admin_commands import admin_commands

def register_events(client: Client, tree: app_commands.CommandTree):
	@client.event
	async def on_ready():
		for guild in client.guilds:
			register_commands(tree, guild)
			await tree.sync(guild=guild)
			await reload_groups(guild)
			V.registered_guilds.add(guild.id)
			LOGGER.msg(f"register commands for {guild.name} ({guild.id})")
		LOGGER.msg(f"{client.user} -- Ready Perfectly !")

	@client.event
	async def on_guild_join(guild: Guild):
		LOGGER.msg(f"I have joined {guild.name} ({guild.id})")
		if guild.id not in V.registered_guilds:
			register_commands(tree, guild)
			V.registered_guilds.add(guild.id)
			LOGGER.msg(f"register commands for {guild.name} ({guild.id})")
		await tree.sync(guild=guild)
		await reload_groups(guild)
		await send_welcome_message(guild)

	@client.event
	async def on_message(message: Message):
		if message.author.bot or message.type != MessageType.default:
			return
		if await admin_commands(message):
			return
		group_channel = await get_group_channel(message.guild)
		if group_channel is not None and message.channel.id == group_channel.id:
			try:
				await message.author.send(MSG.CHANNEL_COMMAND_ONLY % \
						(message.channel.jump_url), suppress_embeds=True)
			except errors.Forbidden:
				LOGGER.msg(f"Could not send message to {message.author.name}" \
						+ f" on {message.guild.name}")
			await message.delete()
