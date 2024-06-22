from discord import Interaction, Embed, Colour
from src.settings.tables import GROUPS_TABLE
from src.settings.variables import GROUP_CHANNEL_ID

async def search(ctx: Interaction, project_name: str):
	data = GROUPS_TABLE.get_data(
			f"{GROUPS_TABLE.project_name} = '{project_name}'",
			GROUPS_TABLE.project_name, GROUPS_TABLE.creator_id,
			GROUPS_TABLE.message_id)
	embed = Embed(color=Colour.from_rgb(255, 0, 0))
	content = ""
	for i, tup in enumerate(data):
		user = await ctx.client.fetch_user(tup[1])
		group_channel = await ctx.client.fetch_channel(GROUP_CHANNEL_ID)
		message = await group_channel.fetch_message(tup[2])
		content += f"{tup[0]} {user.mention} {message.jump_url}"
		if i != len(tup)-1:
			content += "\n"
	if content == "":
		await ctx.response.send_message(f"Project {project_name} not found.")
	else:
		embed.description = content
		await ctx.response.send_message(embed=embed, ephemeral=True)

