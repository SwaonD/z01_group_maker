from discord import ui, Interaction, Embed, Colour, ButtonStyle, Button, User, Member
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import GROUP_CHANNEL_ID
from src.utils.project import is_project, project_exists
from src.utils.group import get_group_id, get_group_members, is_member
from src.utils.log import log
import discord
from typing import Union

class MyView(ui.View):
	def __init__(self, project_name, msg_id, author: Union[User, Member], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.project = project_name
		self.msg_id = msg_id
		self.author = author
	async def show(self):
		print(self)

	@ui.button(label="Join", style=ButtonStyle.primary)
	async def callback1(self, ctx: Interaction, button: Button):
		id = get_group_id(self.msg_id)
  
		if is_member:
			await ctx.response.send_message(":x: You are already in this group !")
			return
  
		GROUP_MEMBERS_TABLE.insert_data(get_group_id(self.msg_id), ctx.user.id)
  
		group_members = get_group_members(id)
  
		embed_desc = f'''
		{self.author.mention} created a group for ```{self.project}```
		'''
		embed = Embed( 
			description=embed_desc,
			title="Group Creation",
			colour=Colour.from_str("#FFF"),
			type="rich"
		)
		usernames = ""
  
		for m in group_members:
			usernames += ctx.client.get_user(m[0]).mention + "\n"
      
		embed.add_field(name="Members", value=usernames, inline=False)
  
		await update_members_count(ctx, self.msg_id, embed=embed)
		await ctx.response.send_message(f"{ctx.user.mention} joined {self.author.mention}'s group", ephemeral=True)

	@ui.button(label="Leave", style=ButtonStyle.secondary)
	async def callback2(self, button: Button, ctx: Interaction):
		await ctx.response.send_message("Button 2 clicked!", ephemeral=True)

async def update_members_count(ctx: Interaction, embed_id: int, embed):
	try:
		# Fetch the partial message by its ID
		message = await ctx.client.get_channel(GROUP_CHANNEL_ID).fetch_message(embed_id)

		# Edit the message with the new embed
		await message.edit(embed=embed)

	except discord.NotFound:
		print(f"Message with ID {embed_id} not found.")
	except discord.Forbidden:
		print("Bot does not have permissions to edit messages.")
	except discord.HTTPException as e:
		print(f"HTTP error occurred: {e}")


async def create_group(ctx: Interaction, project: str):
	# Checks
	if is_project(project) is False:
		await ctx.response.send_message(":x: This project doesn't exist !")
		return

	if  project_exists(project, ctx.user.id) is True:
		await ctx.response.send_message(":x: You already created a group for this project !")
		return

	# Create the embed
	embed_desc = f'''
	{ctx.user.mention} created a group for ```{project}```
	'''
	embed = Embed(
		description=embed_desc,
		title="Group Creation",
		colour=Colour.from_str("#FFF"),
		type="rich"
	)

	embed.add_field(name="Members", value=ctx.user.mention, inline=False)
	log(f'{ctx.user} created a group for {project}', False)

	# Send the embed and get the message object
	message = await ctx.response.send_message(embed=embed)
	message = await ctx.original_response()

 	# Add Group to GROUPDB and Author to the members database
	GROUPS_TABLE.insert_data(message.id, project, ctx.user.id)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(message.id), ctx.user.id)

	v = MyView(project, message.id, ctx.user)
	await message.edit(view=v)

