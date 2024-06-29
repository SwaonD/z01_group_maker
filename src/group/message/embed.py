from discord import Embed, Colour, Client

class GroupMessageEmbed(Embed):
	def __init__(self, client: Client, project_name: str, leader_id: int,
			members_ids: list[int], size_limit: int, description: str,
			confirmed: int):
		usernames: str = ""
		for member_id in members_ids:
			usernames += client.get_user(member_id).mention
			if member_id == leader_id:
				usernames += " :crown:"
			usernames += "\n"
		self.description = description
		self.title = f"{project_name}"
		self.url = ""
		self.type = "rich"
		info_field_name = f"{len(members_ids)}/{size_limit}"
		if confirmed == 1:
			info_field_name += " 🔒"
			self.color = Colour.from_rgb(0, 255, 0)
		else:
			self.color = Colour.from_rgb(255, 255, 255)
		self.add_field(name="Members", value=usernames, inline=True)
		self.add_field(name=info_field_name, value="", inline=True)
