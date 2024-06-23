from discord import Interaction
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.tools import get_group_id, is_member, get_group_members, get_group, Group
from src.group.message.core import update_members_count
from src.utils.log import log


async def join_group(ctx: Interaction):
	group: Group = get_group(ctx.message.id)

	if is_member(group.id, ctx.user.id):
		await ctx.response.send_message(":x: You are already in this group !", ephemeral=True)
		return

	GROUP_MEMBERS_TABLE.insert_data(group.id, ctx.user.id)

	log(f"{ctx.user} joined group {group.id}", None)

	author = ctx.client.get_user(group.creator_id)

	await update_members_count(ctx, group, author)
	await ctx.response.send_message(f"{ctx.user.mention} joined {author.mention}'s group for {group.project_name}", ephemeral=True)


async def leave_group(ctx: Interaction):
	group: Group = get_group(ctx.message.id)

	if is_member(group.id, ctx.user.id) is False:
		await ctx.response.send_message(":x: You are not in this group !", ephemeral=True)
		return

	GROUP_MEMBERS_TABLE.delete_data(
		f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")

	log(f"{ctx.user} left group {group.id}", None)

	author = ctx.client.get_user(group.creator_id)

	await update_members_count(ctx, group, author)
	await ctx.response.send_message(f"{ctx.user.mention} left {author.mention}'s group for {group.project_name}", ephemeral=True)


async def delete_group(ctx: Interaction):
	group: Group = get_group(ctx.message.id)
	if group.creator_id != ctx.user.id:
		await ctx.response.send_message(":x: Only the group creator can delete his group !", ephemeral=True)
		return

	members = get_group_members(group.id)

	for m in members:
		GROUP_MEMBERS_TABLE.delete_data(
			f"{GROUP_MEMBERS_TABLE.id} = {group.id} AND {GROUP_MEMBERS_TABLE.user_id} = {m[0]}")

	GROUPS_TABLE.delete_data(
		f"{GROUPS_TABLE.id} = {get_group_id(ctx.message.id)}")
	await ctx.message.delete()

	log(f"{ctx.user.id} deleted group {group.id}", None)
	await ctx.response.send_message(f"{ctx.user.mention} deleted the {group.project_name} group")
