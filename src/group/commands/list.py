from discord import Interaction, Embed, Colour, TextChannel, PartialMessage, User, Member
from src.settings.tables import GROUPS_TABLE, GROUP_MEMBERS_TABLE
from src.settings.variables import GROUP_CHANNEL_ID

def _get_list_data(project_name: str | None,
		user: User | Member | None) -> tuple[tuple[any]]:
	conditions = []
	user_group_ids = []
	if user is not None:
		user_group_ids_data = GROUP_MEMBERS_TABLE.get_data(
			f"{GROUP_MEMBERS_TABLE.user_id} = {user.id}",
			GROUP_MEMBERS_TABLE.group_id)
		for row in user_group_ids_data:
			user_group_ids.append(row[0])
		if len(user_group_ids) > 0:
			user_group_ids_str = f"({', '.join(map(str, user_group_ids))})"
			conditions.append(
					f"{GROUPS_TABLE.id} IN {str(tuple(user_group_ids_str))}")

	if project_name is not None:
		conditions.append(f"{GROUPS_TABLE.project_name} = '{project_name}'")

	condition = " AND ".join(conditions)
	list_group_data = GROUPS_TABLE.get_data(
				condition, GROUPS_TABLE.project_name,
				GROUPS_TABLE.creator_id, GROUPS_TABLE.message_id)
	return list_group_data

# add option include confirmed group
async def list(ctx: Interaction, project_name: str | None,
		user: User | Member | None):
	data = _get_list_data(project_name, user)
	embed = Embed(color=Colour.from_rgb(255, 0, 0))
	content = ""
	for row in data:
		row_user = ctx.client.get_user(row[1])
		if row_user is None:
			row_user = await ctx.client.fetch_user(row[1])
		group_channel: TextChannel = ctx.client.get_channel(GROUP_CHANNEL_ID)
		if group_channel is None:
			group_channel: TextChannel = \
					await ctx.client.fetch_channel(GROUP_CHANNEL_ID)
		message: PartialMessage = group_channel.get_partial_message(row[2])
		content += f"**{row[0]}** created by {row_user.mention} {message.jump_url}\n"
	if len(content) == 0:
		await ctx.response.send_message("No project found.")
	else:
		embed.description = content
		await ctx.response.send_message(embed=embed, ephemeral=True)

