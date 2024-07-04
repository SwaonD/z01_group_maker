from discord import Interaction, Embed, Colour, User, Member
from src.settings.tables import GROUPS_TABLE, GROUP_MEMBERS_TABLE
from src.settings.variables import MSG, LIST_CMD_CONF_GROUP_MAX
from src.utils.discord import send_quick_response
from src.utils.sql import sql_escape

def _get_list_data(project_name: str | None,
		user: User | Member | None, confirmed: int = 0) -> tuple[tuple[any]]:
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
		conditions.append(
			f"{GROUPS_TABLE.project_name} = '{sql_escape(project_name)}'")

	conditions.append(f"{GROUPS_TABLE.confirmed} = {confirmed}")

	condition = " AND ".join(conditions)
	if confirmed == 1:
		condition += f" ORDER BY {GROUPS_TABLE.project_name} DESC LIMIT " \
				+ str(LIST_CMD_CONF_GROUP_MAX)
	list_group_data = GROUPS_TABLE.get_data(
			condition, GROUPS_TABLE.channel_id, \
			GROUPS_TABLE.message_id, GROUPS_TABLE.project_name)
	return list_group_data

async def _generate_list_content(
		ctx: Interaction, data: tuple[tuple], reverse: bool = False) -> str:
	content = ""
	if reverse:
		i, end = len(data)-1, -1
	else:
		i, end = 0, len(data)
	while i != end:
		channel = ctx.guild.get_channel(data[i][0])
		if channel is None:
			channel = ctx.guild.fetch_channel(data[i][0])
		message = channel.get_partial_message(data[i][1])
		content += MSG.LIST_CONTENT % (data[i][2], message.jump_url)
		if reverse:
			i -= 1
		else:
			i += 1
	return content

async def _create_embed(ctx: Interaction, project_name: str,
		user: User | Member | None, confirm: int, title: str, color: Colour,
		reverse_content: bool = False) -> Embed | None:
	group_data = _get_list_data(project_name, user, confirm)
	grp_content = await _generate_list_content(ctx, group_data, reverse_content)
	if len(grp_content) > 0:
		grp_embed = Embed(color=color)
		grp_embed.description = grp_content
		grp_embed.title = title
		if user is not None:
			grp_embed.set_footer(
					text=user.display_name, icon_url=user.display_avatar.url)
		return grp_embed
	return None

async def list_projects(ctx: Interaction, project_name: str | None,
		user: User | Member | None, show_confirmed_group: bool | None):
	embeds = []
	title = MSG.CURRENT_GROUPS_EMBED_TITLE
	color = Colour.from_rgb(40, 230, 195)
	cur_grp_embed = await _create_embed(ctx, project_name, user, 0, title, color)
	if cur_grp_embed is not None:
		embeds.append(cur_grp_embed)
	if show_confirmed_group is not None and show_confirmed_group is True:
		title = MSG.CONFIRMED_GROUPS_EMBED_TITLE
		color = Colour.from_rgb(0, 255, 0)
		cur_grp_embed = await _create_embed(
				ctx, project_name, user, 1, title, color, True)
		if cur_grp_embed is not None:
			embeds.insert(0, cur_grp_embed)
	if len(embeds) == 0:
		await send_quick_response(ctx, MSG.PROJECT_NOT_FOUND)
	else:
		await ctx.response.send_message(embeds=embeds, ephemeral=True)

