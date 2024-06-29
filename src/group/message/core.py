from discord import Interaction
from src.group.db_request.group import get_group_members_ids, get_group
from src.settings.variables import Group, MSG
from src.settings.tables import GROUPS_TABLE, GROUP_MEMBERS_TABLE
from src.group.message.embed import GroupMessageEmbed
from src.utils.log import LOGGER
from typing import Optional


async def update_embed(ctx: Interaction, message_id: int = 0):
    if ctx.message is None:
        g: Group = get_group(message_id)
        message = ctx.channel.get_partial_message(message_id)
    else:
        g: Group = get_group(ctx.message.id)
        message = ctx.message

    group_members_ids = get_group_members_ids(g.id)
    embed = GroupMessageEmbed(ctx.client, g.project_name, g.leader_id,
                              group_members_ids, g.size_limit, g.description, g.confirmed)
    await message.edit(embed=embed)


async def delete_group(ctx: Interaction, group: Group, members_ids: list[int]):
	for member_id in members_ids:
		if member_id != group.leader_id:
			member = ctx.client.get_user(member_id)
			if member is None:
				member = ctx.client.fetch_user(member_id)
			await member.send(MSG.DELETE_GROUP_TO_MEMBERS % \
					(ctx.user.mention, group.project_name))
	GROUP_MEMBERS_TABLE.delete_data( \
			f"{GROUP_MEMBERS_TABLE.group_id} = {group.id}")
	GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {group.id}")
	await ctx.message.delete()
	LOGGER.msg(f"{ctx.user.name} deleted group {group.id}: {group.project_name}")
