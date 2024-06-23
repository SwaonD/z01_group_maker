from discord import Interaction, User, Member
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE

def _get_user_groups(user: User | Member):
	result = []
	user_group_ids_data = GROUP_MEMBERS_TABLE.get_data(f"{GROUP_MEMBERS_TABLE.user_id} = {user.id}", GROUP_MEMBERS_TABLE.group_id)
	for row in user_group_ids_data:
		groups_data = GROUPS_TABLE.get_data(f"{GROUPS_TABLE.id} = {row[0]}")
		if len(groups_data) > 0:
			result += groups_data[0]
	return result

async def status(ctx: Interaction):
	groups = _get_user_groups(ctx.user)
	print(groups)
	await ctx.response.send_message(content="coucou", ephemeral=True)
