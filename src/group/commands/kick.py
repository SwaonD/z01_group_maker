from discord import Interaction, app_commands, Member
from typing import List
from src.group.db_request.group import  \
	get_all_groups_leader, get_group, is_member, get_group_leader_id
from src.settings.variables import Group
from src.settings.tables import GROUP_MEMBERS_TABLE
from src.utils.log import LOGGER
from src.settings.variables import MSG, Group
from src.utils.discord import send_quick_response
from src.group.message.core import update_embed

async def kick_project_autocompletion(
		ctx: Interaction, current: str) -> List[app_commands.Choice[str]]:
	projects = [
		app_commands.Choice(
			name=group.project_name,
			value=str(group.message_id)
		)
		for group in get_all_groups_leader(ctx.user.id)
		if current in group.project_name or current == ""
	]
	return projects[:20]

async def _is_kick_valid(ctx: Interaction,
		group: Group | None, member: Member) -> bool:
	if group is None:
		await send_quick_response(ctx, MSG.GROUP_NOT_FOUND)
		return False
	leader_id: int = get_group_leader_id(group.message_id)
	if is_member(group.id, member.id) is False:
		await send_quick_response(ctx, MSG.NOT_IN_GROUP)
		return False
	if leader_id != ctx.user.id:
		await send_quick_response(ctx, MSG.NOT_LEADER)
		return False
	if leader_id == member.id:
		await send_quick_response(ctx, MSG.CANT_KICK_LEADER)
		return False
	return True

async def kick_member(ctx: Interaction, project: str, member: Member):
	group: Group = get_group(int(project))
	if not await _is_kick_valid(ctx, group, member):
		return
	GROUP_MEMBERS_TABLE.delete_data(
		f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND"
		+ f" {GROUP_MEMBERS_TABLE.user_id} = {member.id}")
	LOGGER.msg(f"{ctx.user} left group {group.id}")

	channel = ctx.guild.get_channel(group.channel_id)
	msg = channel.get_partial_message(group.message_id)

	await update_embed(ctx, group.message_id)
	await member.send(MSG.MEMBER_KICKED_PM % (ctx.user.mention, msg.jump_url))
	await send_quick_response(ctx,
			MSG.MEMBER_KICKED_CHANNEL % (member.mention, msg.jump_url))
