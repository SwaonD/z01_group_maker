from discord import Interaction, Button
from src.settings.tables import GROUP_MEMBERS_TABLE
from src.utils.group import get_group_id, is_member
from src.group.message.core import update_members_count

async def join_group(self, ctx: Interaction):
	id = get_group_id(ctx.message.id)

	if is_member(id, ctx.user.id):
		await ctx.response.send_message(":x: You are already in this group !", ephemeral=True)
		return

	GROUP_MEMBERS_TABLE.insert_data(id, ctx.user.id)

	await update_members_count(ctx, self.project, self.author)
	await ctx.response.send_message(f"{ctx.user.mention} joined {self.author.mention}'s group for {self.project}", ephemeral=True)

async def leave_group(self, ctx: Interaction):
	id = get_group_id(ctx.message.id)

	if is_member(id, ctx.user.id) is False:
		await ctx.response.send_message(":x: You are not in this group !", ephemeral=True)
		return

	GROUP_MEMBERS_TABLE.delete_data(f"{GROUP_MEMBERS_TABLE.id} = {id} AND {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")

	await update_members_count(ctx, self.project, self.author)
	await ctx.response.send_message(f"{ctx.user.mention} left {self.author.mention}'s group for {self.project}", ephemeral=True)

async def delete_group(self, ctx: Interaction, button: Button):
	await ctx.response.send_message("delete")
