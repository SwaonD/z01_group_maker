from discord import Interaction, Embed, Colour
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.tools import is_project, project_exists
from src.group.message.tools import get_group_id
from src.utils.log import log
from src.group.message.view import GroupMessageView

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

	v = GroupMessageView(project, ctx.user)

	# Send the embed and get the message object
	message = await ctx.response.send_message(embed=embed, view=v)
	message = await ctx.original_response()

 	# Add Group to GROUPDB and Author to the members database
	GROUPS_TABLE.insert_data(message.id, project, ctx.user.id)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(message.id), ctx.user.id)
