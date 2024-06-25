from discord import Interaction
from src.group.message.db_request import is_member, \
		get_group_members_ids, Group, get_group
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import NOTIF_MSG_TIMEOUT, MSG_LOG_FILE_PATH
from src.group.message.core import update_embed
from src.utils.log import log
from src.group.message.modal import Confirm

async def join_group(ctx: Interaction, group: Group):
	if is_member(group.id, ctx.user.id):
		await ctx.response.send_message(":x: You are already in this group !",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return
	if group.confirmed == 1:
		await ctx.response.send_message(":lock: This group is locked, you cannot"
				f" join it !", ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return
	group_len = len(get_group_members_ids(group.id))
	if group_len + 1 > group.size_limit:
		await ctx.response.send_message(":x: This group is full",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return
	GROUP_MEMBERS_TABLE.insert_data(group.id, ctx.user.id)

	log(f"{ctx.user} joined group {group.id}", MSG_LOG_FILE_PATH)

	author = ctx.client.get_user(group.leader_id)
	message_to_leader = f"{ctx.user.mention} joined your group !"
	if group_len + 1 == group.size_limit:
		message_to_leader += " Your group is now full !"
	await author.send(message_to_leader)

	if author is None:
		author = await ctx.client.fetch_user(group.leader_id)

	await update_embed(ctx)
	await ctx.response.send_message(
			f"{ctx.user.mention} joined {author.mention}'s group for"
			+ f" {group.project_name}", ephemeral=True,
			delete_after=NOTIF_MSG_TIMEOUT)


async def leave_group(ctx: Interaction, group: Group):
	if is_member(group.id, ctx.user.id) is False:
		await ctx.response.send_message(":x: You are not in this group !",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return
	if group.confirmed == 1:
		await ctx.response.send_message(
				":lock: This group is locked, you cannot leave it !",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return
	GROUP_MEMBERS_TABLE.delete_data(
			f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND"
			+ f" {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")
	log(f"{ctx.user} left group {group.id}", MSG_LOG_FILE_PATH)

	g: Group = get_group(ctx.message.id)
	group_members_ids = get_group_members_ids(g.id)

	if len(group_members_ids) == 0:
		GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {group.id}")
		await ctx.response.send_message(
				f":cry: No one left in the group ! It was deleted",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		await ctx.message.delete()
		return
	# delete when no members left

	isNewLeader = False
	if ctx.user.id == group.leader_id:
		data = {
			GROUPS_TABLE.leader_id: group_members_ids[0]
		}
		GROUPS_TABLE.update_data(data, f"{GROUPS_TABLE.id} = {g.id}")
		group.leader_id = group_members_ids[0]
		isNewLeader = True
	# update leader if there is only one person left.

	leader = ctx.client.get_user(group.leader_id)
	if leader is None:
		leader = await ctx.client.fetch_user(group.leader_id)
	await leader.send(f"{ctx.user.mention} left your group {group.project_name}!"
			+ f"{ctx.message.jump_url}")
	if isNewLeader:
		await leader.send(
				f"You are now the new group leader of {group.project_name}!"
				+ f" {ctx.message.jump_url}")

	await update_embed(ctx)
	await ctx.response.send_message(
			f"You have successfully left the group {group.project_name}.",
			ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)


async def confirm_group(ctx: Interaction, group: Group):
	group_members_ids = get_group_members_ids(group.id)
	if len(group_members_ids) <= 1:
		await ctx.response.send_message(
				":x: You can only confirm a group with a minimum of 2 people !",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return

	if ctx.user.id != group.leader_id:
		await ctx.response.send_message(
				":x: Only the group leader can confirm his group !",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return

	for member_id in group_members_ids:
		await ctx.client.get_user(member_id).send(
				f"You group leader {ctx.client.get_user(group.leader_id)}"
				+ f" confirmed the group for {group.project_name}")

	data = {}
	stat = ""

	if group.confirmed == 1:
		data = {
			GROUPS_TABLE.confirmed: 0
		}
		stat = "unconfirmed"
	else:
		data = {
			GROUPS_TABLE.confirmed: 1
		}
		stat = "confirmed"

	GROUPS_TABLE.update_data(
		data, f"{GROUPS_TABLE.message_id} = {group.message_id}")

	await update_embed(ctx)
	await ctx.response.send_message(
			f"{ctx.user.mention} {stat} the {group.project_name} project",
			ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)


async def delete_group(ctx: Interaction, group: Group):
	if ctx.user.id != group.leader_id:
		await ctx.response.send_message(
				":x: Only the leader can delete the group !",
				ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
		return
	await ctx.response.send_modal(Confirm(group))
