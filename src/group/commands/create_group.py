from discord import Interaction
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.db_request import is_project, project_exists
from src.group.message.db_request import get_group_id
from src.group.message.view import GroupMessageView
from src.group.message.embed import GroupMessageEmbed

async def create_group(ctx: Interaction,
		project_name: str, size_limit: int, description: str | None):
	if is_project(project_name) is False:
		await ctx.response.send_message(":x: This project doesn't exist !",
				ephemeral=True, delete_after=5.0)
		return
	if project_exists(project_name, ctx.user.id) is True:
		await ctx.response.send_message(
				":x: You already created a group for this project !",
				ephemeral=True, delete_after=5.0)
		return
	if size_limit < 2:
		await ctx.response.send_message(
				":x: The size limit must be upper than 1 !"
		)
		return
	if description is None:
		description = ""
	confirmed = 0
	embed = GroupMessageEmbed(ctx.client, project_name, ctx.user.id,
			[ctx.user.id], size_limit, description, confirmed)
	view = GroupMessageView(project_name, ctx.user)
	await ctx.response.send_message(embed=embed, view=view)
	message = await ctx.original_response()
	# Send the embed and get the message object
	GROUPS_TABLE.insert_data(message.id,
			project_name, ctx.user.id, size_limit, description, confirmed)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(message.id), ctx.user.id)
	# Add Group to GROUPDB and Author to the members database
