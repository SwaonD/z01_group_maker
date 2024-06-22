from discord import ui, Interaction, Embed, Colour, ButtonStyle, Button
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.utils.project import is_project, project_exists
from src.utils.group import get_group_id, get_group_members
import logging

class MyView(ui.View):
	def __init__(self, project_name, interaction_id, author: str, *args, **kwargs):
		super().__init__(*args, **kwargs) 
		self.project = project_name
		self.interaction_id = interaction_id
		self.author = author
	async def show(self):
		print(self)
		
	@ui.button(label="Join", style=ButtonStyle.success)
	async def callback1(self, button: Button, ctx: Interaction):
		id = get_group_id(self.interaction_id)
		get_group_members(id)
		# GROUPS_TABLE.insert_data(self.interaction_id, self.project, self.author)
		# GROUP_MEMBERS_TABLE.insert_data(get_group_id(self.interaction_id), self.author)
		await ctx.response.send_message(f"{ctx.user.mention} joined {self.author.mention}'s group", ephemeral=True)

	@ui.button(label="Leave", style=ButtonStyle.danger)
	async def callback2(self, button: Button, ctx: Interaction):
		await ctx.response.send_message("Button 2 clicked!", ephemeral=True)

async def update_members_count(ctx: Interaction, embed_id: int):
    message_id = embed_id

async def create_group(ctx: Interaction, project:str):
    # Checks
	if is_project(project) is False:
		await ctx.response.send_message(":x: This project doesn't exist !")
		return

	if  project_exists(project, ctx.user) is True:
		await ctx.response.send_message(":x: You already created a group for this project !")
		return

	# Add Group to GROUPDB and Author to MEMBERSDB
	GROUPS_TABLE.insert_data(ctx.id, project, ctx.user.id)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(ctx.id), ctx.user.id)

	# Embed
	embed_desc = f'''
	{ctx.user.mention} created a group for ```{project}```
	'''
	embed = Embed(
		description=embed_desc,	
		title="Group Creation",
		colour=Colour.from_str("#FFF"),
		type="rich"
	)

	embed.add_field(name="Members", value="0", inline=False)
	logging.info(f'{ctx.user} created a group for {project}')
	
	v = MyView(project, ctx.id, ctx.user)
	await ctx.response.send_message(embed=embed, view=v)
