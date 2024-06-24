from src.group.message.tools import is_member, get_group_members, Group, get_group
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.core import update_embed
from discord import Interaction
from src.utils.log import log
from src.group.message.modal import Confirm

async def join_group(ctx: Interaction, group: Group):
	if is_member(group.id, ctx.user.id):
		await ctx.response.send_message(":x: You are already in this group !",
				ephemeral=True, delete_after=5.0)
		return
	if group.confirmed == 1:
		await ctx.response.send_message(":lock: This group is locked, you cannot"
				f" join it !", ephemeral=True, delete_after=5.0)
		return
	group_len = len(get_group_members(group.id))
	if group_len + 1 > group.size_limit:
		await ctx.response.send_message(":x: This group is full",
				ephemeral=True, delete_after=5.0)
		return
	GROUP_MEMBERS_TABLE.insert_data(group.id, ctx.user.id)

	log(f"{ctx.user} joined group {group.id}", None)

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
			+ f" {group.project_name}", ephemeral=True, delete_after=5.0)


async def leave_group(ctx: Interaction, group: Group):
	if is_member(group.id, ctx.user.id) is False:
		await ctx.response.send_message(":x: You are not in this group !",
				ephemeral=True, delete_after=5.0)
		return
	if group.confirmed == 1:
		await ctx.response.send_message(
				":lock: This group is locked, you cannot leave it !",
				ephemeral=True, delete_after=5.0)
		return
	GROUP_MEMBERS_TABLE.delete_data(
			f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND"
			+ f" {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")
	log(f"{ctx.user} left group {group.id}", None)

	g: Group = get_group(ctx.message.id)
	group_members = get_group_members(g.id)

	author = ctx.client.get_user(group.leader_id)
	await author.send(f"{ctx.user.mention} left your group !")

	if author is None:
		author = await ctx.client.fetch_user(group.leader_id)

	if len(group_members) == 0:
		GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {group.id}")
		await ctx.response.send_message(
				f":cry: No one left in the group ! It was deleted",
				ephemeral=True, delete_after=5.0)
		await ctx.message.delete()
		return
	# delete when no members left
	if len(group_members) == 1:
		last_member = ctx.client.get_user(group_members[0][0])
		data = {
			GROUPS_TABLE.leader_id: group_members[0][0]
		}
		GROUPS_TABLE.update_data(data, f"{GROUPS_TABLE.id} = {g.id}")
		await update_embed(ctx)
		await ctx.response.send_message(
				f"You left {author.mention}'s group. {last_member.mention}"
				+ f" is the new leader.", ephemeral=True, delete_after=5.0)
		return
	# update leader if there is only one person left.
	await update_embed(ctx)
	await ctx.response.send_message(
			f"You left {author.mention}'s group for {group.project_name}",
			ephemeral=True, delete_after=5.0)


async def confirm_group(ctx: Interaction, group: Group):
	group_members = get_group_members(group.id)
	if len(group_members) <= 1:
		await ctx.response.send_message(
				":x: You can only confirm a group with a minimum of 2 people !",
				ephemeral=True, delete_after=5.0)
		return

	if ctx.user.id != group.leader_id:
		await ctx.response.send_message(
				":x: Only the group leader can confirm his group !",
				ephemeral=True, delete_after=5.0)
		return

	for m in group_members:
		await ctx.client.get_user(m[0]).send(
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
			ephemeral=True, delete_after=5.0)


async def delete_group(ctx: Interaction, group: Group):
	await ctx.response.send_modal(Confirm(group))
