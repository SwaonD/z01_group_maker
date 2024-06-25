from discord import Interaction
from src.group.message.db_request import get_group_members_ids, get_group
from src.settings.variables import Group
from src.group.message.embed import GroupMessageEmbed

async def update_embed(ctx: Interaction):
	g: Group = get_group(ctx.message.id)
	group_members_ids = get_group_members_ids(g.id)
	embed = GroupMessageEmbed(ctx.client, g.project_name, g.leader_id,
			group_members_ids, g.size_limit, g.description, g.confirmed)
	await ctx.message.edit(embed=embed)
