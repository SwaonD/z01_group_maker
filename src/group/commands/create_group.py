from discord import Interaction, Embed, Colour, User, Member
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.tools import is_project, project_exists
from src.group.message.tools import get_group_id
from src.utils.log import log
from src.group.message.view import GroupMessageView


async def create_group(ctx: Interaction,
		project_name: str, size_limit: int, description: str | None):
	if is_project(project_name) is False:
		await ctx.response.send_message(":x: This project doesn't exist !",
				ephemeral=True, delete_after=5.0)
		return
	if project_exists(project_name, ctx.user.id) is True:
		await ctx.response.send_message(
				":x: You already created a group for this project !",
				ephemeral=True, delete_after=5.0)
		return
	if size_limit < 2:
		await ctx.response.send_message(
				":x: The size limit must be upper than 1 !"
		)
		return
	if description is None:
		description = ""
	embed, view = generate_basic_group_embed(
			ctx.user, project_name, size_limit, description)
	message = await ctx.response.send_message(embed=embed, view=view)
	message = await ctx.original_response()
	# Send the embed and get the message object
	GROUPS_TABLE.insert_data(message.id,
			project_name, ctx.user.id, size_limit, description)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(message.id), ctx.user.id)
	# Add Group to GROUPDB and Author to the members database

def generate_basic_group_embed(leader: User | Member, project_name: str,
		size_limit: int, description: str) -> tuple[Embed, GroupMessageView]:
	embed = Embed(
		description=description,
		title=f"{project_name}    1/{size_limit}",
		colour=Colour.from_rgb(255, 255, 255),
		type="rich"
	)
	embed.add_field(
		name="Members", value=f"{leader.mention} :crown:", inline=False)
	embed.add_field(
		name="Status", value=":unlock: Not confirmed yet !", inline=False)
	log(f'{leader} created a group for {project_name}', False)
	view = GroupMessageView(project_name, leader)
	return (embed, view)
