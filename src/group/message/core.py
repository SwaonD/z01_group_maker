from discord import Interaction, Embed, Colour
from src.settings.tables import GROUPS_TABLE
from src.group.message.tools import get_group_id, get_group_members, Group

async def update_members_count(ctx: Interaction, group: Group, author):
	group_members = get_group_members(group.id)
	print(group_members, len(group_members))
	if len(group_members) == 0:
		GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {get_group_id(ctx.message.id)}")
		await ctx.message.delete()
		return

	embed_desc: str = f'''
	{author.mention} created a group for ```{group.project_name}```
	'''
	embed: Embed = Embed(
		description=embed_desc,
		title="Group Creation",
		colour=Colour.from_str("#FFF"),
		type="rich"
	)

	usernames: str = ""
	for m in group_members:
		usernames += ctx.client.get_user(m[0]).mention + "\n"

	embed.add_field(name="Members", value=usernames, inline=False)
	# Edit the message with the new embed
	await ctx.message.edit(embed=embed)
