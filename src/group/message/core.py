from discord import Interaction
from src.group.message.db_request import get_group_members_ids, get_group, get_group_id
from src.settings.variables import Group, MSG, MSG_LOG_FILE_PATH
from src.settings.tables import GROUPS_TABLE, GROUP_MEMBERS_TABLE
from src.group.message.embed import GroupMessageEmbed
from src.utils.discord import send_quick_response
from src.utils.log import log

async def update_embed(ctx: Interaction):
	g: Group = get_group(ctx.message.id)
	group_members_ids = get_group_members_ids(g.id)
	embed = GroupMessageEmbed(ctx.client, g.project_name, g.leader_id,
			group_members_ids, g.size_limit, g.description, g.confirmed)
	await ctx.message.edit(embed=embed)

async def delete_group(ctx: Interaction, group: Group, members_ids: list[int]):
	for member_id in members_ids:
		if member_id != group.leader_id:
			member = ctx.client.get_user(member_id)
			if member is None:
				member = ctx.client.fetch_user(member_id)
			await member.send(MSG.DELETE_GROUP_TO_MEMBERS)
		GROUP_MEMBERS_TABLE.delete_data(
			f"{GROUP_MEMBERS_TABLE.id} = {group.id} AND"
			+ f" {GROUP_MEMBERS_TABLE.user_id} = {member_id}")
	GROUPS_TABLE.delete_data(
		f"{GROUPS_TABLE.id} = {get_group_id(group.message_id)}")
	await ctx.message.delete()
	log(f"{ctx.user.id} deleted group {group.id}", MSG_LOG_FILE_PATH)
