from discord import Embed, Colour, Client


class WelcomeMessageEmbed(Embed):
	def __init__(self):
		self.url = ""
		self.description = """
		This bot helps creating groups to work together !
		:bangbang: **Before using this bot don't forget to set up a channel ID with the /config <channel_id> command !**
  		:page_facing_up: Here is a list of the commands available: 
  		"""
		self.title = f"Welcome Group Maker !"
		self.type = "rich"
		self.add_field(name="/create", value="Create a group, takes as arguments the project name, a size and an optional description", inline=False)
		self.add_field(name="/list", value="Lists every group available, arguments are optional, they are used to filter by user or project name", inline=False)
		self.add_field(name="/status", value="Displays the current groups you are in or the groups you created", inline=False)
		self.add_field(name="/config", value="Takes as argument the channel ID you want the bot to send messages on", inline=False)
		self.add_field(name="/kick", value="Kicks someone from a group whose leader is you, takes as argument a project name and a user to kick", inline=False)
		self.add_field(name="/reload_groups", value="Reload all the group messages if the buttons dont work", inline=False)