from discord import Interaction, Embed, Colour, TextChannel, PartialMessage
from src.settings.tables import GROUPS_TABLE
from src.settings.variables import GROUP_CHANNEL_ID_S

async def list(ctx: Interaction, project_name: str | None):
	condition = ""
	if project_name is not None:
		condition = f"{GROUPS_TABLE.project_name} = '{project_name}'"
	data = GROUPS_TABLE.get_data(
			condition, GROUPS_TABLE.project_name,
			GROUPS_TABLE.creator_id, GROUPS_TABLE.message_id)
	embed = Embed(color=Colour.from_rgb(255, 0, 0))
	content = ""
	for tup in data:
		user = ctx.client.get_user(tup[1])
		if user is None:
			user = await ctx.client.fetch_user(tup[1])
		group_channel: TextChannel = ctx.client.get_channel(GROUP_CHANNEL_ID_S)
		if group_channel is None:
			group_channel: TextChannel = \
					await ctx.client.fetch_channel(GROUP_CHANNEL_ID_S)
		message: PartialMessage = group_channel.get_partial_message(tup[2])
		content += f"{tup[0]} {user.mention} {message.jump_url}\n"
	if content == "":
		await ctx.response.send_message(f"Project {project_name} not found.")
	else:
		embed.description = content
		await ctx.response.send_message(embed=embed, ephemeral=True)

