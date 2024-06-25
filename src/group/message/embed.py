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
		msg = ""
		emoji = ""
		if confirmed == 1:
			msg = "This group is confirmed !"
			self.color = Colour.from_rgb(0, 255, 0)
			emoji = ":lock: "
		else:
			msg = "Not confirmed yet !"
			self.color = Colour.from_rgb(255, 255, 255)
			emoji = ":unlock: "
		self.description = description
		self.title = f"{project_name}    {len(members_ids)}/{size_limit}"
		self.url = ""
		self.type = "rich"
		self.add_field(name="Members", value=usernames, inline=False)
		self.add_field(name="Status", value=emoji+msg, inline=False)
