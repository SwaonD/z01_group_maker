from discord import Interaction, app_commands
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import MSG, Variables as V
from src.utils.discord import send_quick_response
from src.group.db_request.project import is_project, project_exists
from src.group.db_request.config import get_group_channel
from src.group.message.view import GroupMessageView
from src.group.message.embed import GroupMessageEmbed
from fuzzywuzzy import fuzz
from typing import List

async def create_group(ctx: Interaction,
		project_name: str, size_limit: int, description: str | None):
	group_channel = await get_group_channel(ctx.guild)
	if group_channel is None:
		await send_quick_response(ctx, MSG.GROUP_CHANNEL_NOT_CONFIGURED)
		return
	if not await _is_input_valid(ctx, project_name, size_limit):
		return
	if description is None:
		description = ""
	confirmed = 0
	embed = GroupMessageEmbed(ctx.client, project_name, ctx.user.id,
			[ctx.user.id], size_limit, description, confirmed)
	view = GroupMessageView()
	if ctx.channel.id == group_channel.id:
		await ctx.response.send_message(embed=embed, view=view)
		message = await ctx.original_response()
	else:
		message = await group_channel.send(embed=embed, view=view)
		await send_quick_response(ctx,
			MSG.GROUP_CREATED % (project_name, message.jump_url), 10)
	# Send the embed and get the message object
	group_id = GROUPS_TABLE.insert_data(ctx.guild.id, \
			message.channel.id, message.id, project_name, \
			ctx.user.id, size_limit, description, confirmed)
	GROUP_MEMBERS_TABLE.insert_data(group_id, ctx.user.id)
	# Add Group to GROUPDB and Author to the members database

async def _is_input_valid(ctx: Interaction,
		project_name: str, size_limit: int) -> bool:
	if is_project(project_name) is False:
		await send_quick_response(ctx,
				MSG.PROJECTS_DOES_NOT_EXISTS % (project_name))
		return False
	if project_exists(project_name, ctx.user.id) is True:
		await send_quick_response(ctx, MSG.GROUP_ALREADY_EXISTS)
		return False
	if size_limit < 2:
		await send_quick_response(ctx, MSG.HAS_NOT_MINIMUM_SIZE)
		return False
	return True

async def project_names_autocompletion(
		ctx: Interaction, current: str) -> List[app_commands.Choice[str]]:
	if not current.strip():
		return [app_commands.Choice(name=project_name, value=project_name) for project_name in V.project_names]
	filtered_projects = [name for name in V.project_names \
			if current.lower() in name.lower()][:25]
	filtered_projects.sort(key=lambda name: \
			fuzz.partial_ratio(current.lower(), name.lower()), reverse=True)
	filtered_projects = filtered_projects[:10]
	choices = [app_commands.Choice(name=project_name, value=project_name) \
			for project_name in filtered_projects]
	return choices
