from discord import Interaction
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import MSG
from src.utils.discord import send_quick_response
from src.group.message.db_request import is_project, project_exists
from src.group.message.db_request import get_group_id
from src.group.message.view import GroupMessageView
from src.group.message.embed import GroupMessageEmbed

async def create_group(ctx: Interaction,
		project_name: str, size_limit: int, description: str | None):
	if not await _is_input_valid(ctx, project_name, size_limit):
		return
	if description is None:
		description = ""
	confirmed = 0
	embed = GroupMessageEmbed(ctx.client, project_name, ctx.user.id,
			[ctx.user.id], size_limit, description, confirmed)
	view = GroupMessageView()
	await ctx.response.send_message(embed=embed, view=view)
	message = await ctx.original_response()
	# Send the embed and get the message object
	GROUPS_TABLE.insert_data(message.id,
			project_name, ctx.user.id, size_limit, description, confirmed)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(message.id), ctx.user.id)
	# Add Group to GROUPDB and Author to the members database

async def _is_input_valid(ctx: Interaction,
		project_name: str, size_limit: int) -> bool:
	if is_project(project_name) is False:
		await send_quick_response(ctx, MSG.PROJECTS_DOES_NOT_EXISTS)
		return False
	if project_exists(project_name, ctx.user.id) is True:
		await send_quick_response(ctx, MSG.GROUP_ALREADY_EXISTS)
		return False
	if size_limit < 2:
		await send_quick_response(ctx, MSG.HAS_NOT_MINIMUM_SIZE)
		return False
	return True
