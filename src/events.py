from discord import Client, app_commands, Guild, Message, MessageType, errors
from src.init import reload_groups
from src.commands import register_commands
from src.utils.log import LOGGER
from src.utils.discord import send_private_message
from src.group.db_request.config import get_group_channel_id
from src.settings.variables import MSG, Variables as V
from src.welcome import send_welcome_message
from src.admin_commands import admin_commands


async def handle_message_in_group_channel(message: Message):
	if message.guild is None:
		return
	group_channel_id = get_group_channel_id(message.guild)
	if group_channel_id is not None and message.channel.id == group_channel_id:
		try:
			if not message.author.bot:
				await send_private_message(message.author, \
						MSG.CHANNEL_COMMAND_ONLY % (message.channel.jump_url))
			await message.delete()
		except errors.Forbidden:
			LOGGER.msg(f"Could not delete message {message.jump_url}.")

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
		if message.author == client.user:
			return
		if await admin_commands(client, message):
			return
		await handle_message_in_group_channel(message)
