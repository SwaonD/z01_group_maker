from discord import Interaction, Member
from src.group.db_request.group import is_member, get_group_members_ids
from src.group.message.core import update_embed, delete_group
from src.utils.discord import send_quick_response, send_private_message
from src.utils.log import LOGGER
from src.group.message.modal import ConfirmDeleteGroup
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import MSG, Group


async def join_group(ctx: Interaction, group: Group):
	if is_member(group.id, ctx.user.id):
		await send_quick_response(ctx, MSG.ALREADY_IN_GROUP)
		return
	if group.confirmed == 1:
		await send_quick_response(ctx, MSG.GROUP_LOCKED_CANT_JOIN)
		return
	group_len = len(get_group_members_ids(group.id))
	if group_len + 1 > group.size_limit:
		await send_quick_response(ctx, MSG.GROUP_IS_FULL)
		return
	GROUP_MEMBERS_TABLE.insert_data(group.id, ctx.user.id)
	LOGGER.msg(f"{ctx.user} joined group {group.id}")

	author = ctx.client.get_user(group.leader_id)
	if author is None:
		author = await ctx.client.fetch_user(group.leader_id)
	message_to_leader = MSG.USER_JOIN_GROUP_TO_LEADER % \
		(ctx.user.mention, group.project_name, ctx.message.jump_url)
	if group_len + 1 == group.size_limit:
		message_to_leader += "\n" + MSG.GROUP_IS_FULL_TO_LEADER
	await send_private_message(author, message_to_leader)

	await update_embed(ctx)
	await send_quick_response(ctx, MSG.USER_JOIN_GROUP % (group.project_name))


async def _update_group_leader_on_leave(ctx: Interaction,
		group: Group, group_members_ids: list[int]) -> Member | None:
	if len(group_members_ids) == 0:
		return None
	if ctx.user.id == group.leader_id:
		data = {
			GROUPS_TABLE.leader_id: group_members_ids[0]
		}
		GROUPS_TABLE.update_data(data, f"{GROUPS_TABLE.id} = {group.id}")
		group.leader_id = group_members_ids[0]
	leader = ctx.guild.get_member(group.leader_id)
	if leader is None:
		leader = await ctx.guild.fetch_member(group.leader_id)
	return leader

async def leave_group(ctx: Interaction, group: Group):
	if is_member(group.id, ctx.user.id) is False:
		await send_quick_response(ctx, MSG.NOT_IN_GROUP)
		return
	if group.confirmed == 1:
		await send_quick_response(ctx, MSG.GROUP_LOCKED_CANT_LEAVE)
		return
	GROUP_MEMBERS_TABLE.delete_data(
			f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND"
			+ f" {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")
	LOGGER.msg(f"{ctx.user} left group {group.id}")
	group_members_ids = get_group_members_ids(group.id)
	if len(group_members_ids) == 0:
		await delete_group(ctx, group, group_members_ids)
		await send_quick_response(ctx, MSG.DELETE_EMPTY_GROUP)
		# delete when no members left
		return
	leader = await _update_group_leader_on_leave(ctx, group, group_members_ids)
	# send messages
	await send_private_message(leader, MSG.USER_LEFT_GROUP_TO_LEADER % \
			(ctx.user.mention, group.project_name, ctx.message.jump_url))
	if leader.id != ctx.user.id:
		await send_private_message(leader, MSG.NEW_GROUP_LEADER % \
				(group.project_name, ctx.message.jump_url))
	await update_embed(ctx)
	await send_quick_response(ctx, MSG.USER_LEFT_GROUP % (group.project_name))


async def confirm_group(ctx: Interaction, group: Group):
	group_members_ids = get_group_members_ids(group.id)
	if ctx.user.id not in group_members_ids:
		await send_quick_response(ctx, MSG.NOT_IN_GROUP)
		return
	if len(group_members_ids) <= 1:
		await send_quick_response(ctx, MSG.CONFIRM_GROUP_MINIMUM_SIZE)
		return
	if ctx.user.id != group.leader_id:
		await send_quick_response(ctx, MSG.CONFIRM_GROUP_NOT_AUTHORIZED)
		return
	leader = ctx.client.get_user(group.leader_id)
	if leader is None:
		leader = ctx.client.fetch_user(group.leader_id)


	data = {}
	status = ""
	if group.confirmed == 1:
		data = {
			GROUPS_TABLE.confirmed: 0
		}
		status = MSG.CONFIRM_GROUP_STATUS_UNLOCKED
	else:
		data = {
			GROUPS_TABLE.confirmed: 1
		}
		status = MSG.CONFIRM_GROUP_STATUS_CONFIRMED
	GROUPS_TABLE.update_data(
		data, f"{GROUPS_TABLE.message_id} = {group.message_id}")

	for member_id in group_members_ids:
		if member_id != group.leader_id:
			member = ctx.client.get_user(member_id)
			if member is None and data[GROUPS_TABLE.confirmed] == 1:
				member = ctx.client.fetch_user(member_id)
			await send_private_message(member, MSG.CONFIRM_GROUP_TO_MEMBERS %
					(leader.mention, group.project_name, ctx.message.jump_url))


	await update_embed(ctx)
	await send_quick_response(ctx, MSG.CONFIRM_GROUP %
							  (status, group.project_name))


async def delete_group_from_button(ctx: Interaction, group: Group):
	if not is_member(group.id, ctx.user.id):
		await send_quick_response(ctx, MSG.NOT_IN_GROUP)
		return
	if ctx.user.id != group.leader_id:
		await send_quick_response(ctx, MSG.DELETE_GROUP_NOT_AUTHORIZE)
		return
	await ctx.response.send_modal(ConfirmDeleteGroup(group,
					MSG.DELETE_GROUP_MODAL_TITLE % (group.project_name)))
