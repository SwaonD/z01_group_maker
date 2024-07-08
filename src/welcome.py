from discord import Embed, Guild, TextChannel
from src.settings.variables import MSG

class WelcomeMessageEmbed(Embed):
	def __init__(self):
		self.url = ""
		self.title = MSG.WELCOME_TITLE
		self.description = MSG.WELCOME_DESCRIPTION
		self.type = "rich"
		self.add_field(name="/create", value=MSG.WELCOME_CREATE_CMD, inline=False)
		self.add_field(name="/list", value=MSG.WELCOME_LIST_CMD, inline=False)
		self.add_field(name="/status", value=MSG.WELCOME_STATUS_CMD, inline=False)
		self.add_field(name="/config", value=MSG.WELCOME_CONFIG_CMD, inline=False)
		self.add_field(name="/kick", value=MSG.WELCOME_KICK_CMD, inline=False)
		self.set_image(url="https://i.imgur.com/D8VWzWV.gif")

async def send_welcome_message(guild: Guild):
	for channel in guild.channels:
		if isinstance(channel, TextChannel):
			bot_permissions = channel.permissions_for(guild.me)
			if bot_permissions.send_messages:
				await channel.send(embed=WelcomeMessageEmbed())
				return
