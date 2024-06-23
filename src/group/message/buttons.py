from src.group.message.tools import is_member, get_group_members, Group, get_group
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.core import update_embed
from discord import Interaction, ui
from src.utils.log import log
from src.group.message.modal import Confirm

view: ui.View

async def join_group(ctx: Interaction, group: Group):
    if is_member(group.id, ctx.user.id):
        await ctx.response.send_message(":x: You are already in this group !", ephemeral=True, delete_after=5.0)
        return

    if group.confirmed == 1:
        await ctx.response.send_message(":lock: This group is locked, you cannot join it !", ephemeral=True, delete_after=5.0)
        return

    GROUP_MEMBERS_TABLE.insert_data(group.id, ctx.user.id)

    log(f"{ctx.user} joined group {group.id}", None)

    author = ctx.client.get_user(group.creator_id)

    if author is None:
        author = await ctx.client.fetch_user(group.creator_id)

    await update_embed(ctx)
    await ctx.response.send_message(f"{ctx.user.mention} joined {author.mention}'s group for {group.project_name}", ephemeral=True, delete_after=5.0)


async def leave_group(ctx: Interaction, group: Group):
    if is_member(group.id, ctx.user.id) is False:
        await ctx.response.send_message(":x: You are not in this group !", ephemeral=True, delete_after=5.0)
        return

    if group.confirmed == 1:
        await ctx.response.send_message(":lock: This group is locked, you cannot leave it !", ephemeral=True, delete_after=5.0)
        return

    GROUP_MEMBERS_TABLE.delete_data(
        f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")

    log(f"{ctx.user} left group {group.id}", None)

    g: Group = get_group(ctx.message.id)
    group_members = get_group_members(g.id)

    author = ctx.client.get_user(group.creator_id)

    if author is None:
        author = await ctx.client.fetch_user(group.creator_id)

    if len(group_members) == 0:
        GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {group.id}")
        await ctx.response.send_message(f":cry: No one left in the group ! It was deleted", ephemeral=True, delete_after=5.0)
        await ctx.message.delete()
        return

    if len(group_members) == 1:
        last_member = ctx.client.get_user(group_members[0][0])
        data = {
            GROUPS_TABLE.creator_id: group_members[0][0]
        }
        GROUPS_TABLE.update_data(data, f"{GROUPS_TABLE.id} = {g.id}")
        await update_embed(ctx)
        await ctx.response.send_message(f"You left {author.mention}'s group. {last_member.mention} is the new leader.", ephemeral=True, delete_after=5.0)
        return

    await update_embed(ctx)
    await ctx.response.send_message(f"You left {author.mention}'s group for {group.project_name}", ephemeral=True, delete_after=5.0)


async def confirm_group(ctx: Interaction, group: Group):
    
    group_members = get_group_members(group.id)
    if len(group_members) <= 1:
        await ctx.response.send_message(":x: You can only confirm a group with a minimum of 2 people !", ephemeral=True, delete_after=5.0)
        return

    if ctx.user.id != group.creator_id:
        await ctx.response.send_message(":x: Only the group leader can confirm his group !", ephemeral=True, delete_after=5.0)
        return

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
    await ctx.response.send_message(f"{ctx.user.mention} {stat} the {group.project_name} project", ephemeral=True, delete_after=5.0)


async def delete_group(ctx: Interaction, group: Group):
    await ctx.response.send_modal(Confirm(group))
