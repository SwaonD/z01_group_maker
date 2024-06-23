from discord import Interaction, Embed, Colour, User, Member

from src.group.message.tools import get_group_members, get_group, Group


async def update_embed(ctx: Interaction, group: Group, author: User | Member):
	group_members = get_group_members(group.id)

	usernames: str = ""
	for m in group_members:
		usernames += ctx.client.get_user(m[0]).mention + "\n"

	g: Group = get_group(ctx.message.id)

	msg = ""
	color = ""
	emoji = ""

	if g.confirmed == 1:
		msg = "This group is confirmed !"
		color = "#008000"
		emoji = ":lock: "
	else:
		msg = "Not confirmed yet !"
		color = "#FFF"
		emoji = ":unlock: "

	embed_desc: str = f'''
	{author.mention} created a group for ```{group.project_name}```
	'''
	embed: Embed = Embed(
		description=embed_desc,
		title="Group Creation",
		colour=Colour.from_str(color),
		type="rich"
	)

	embed.add_field(name="Members", value=usernames, inline=False)
	embed.add_field(name="Status", value=emoji+msg, inline=False)
	# Edit the message with the new embed
	await ctx.message.edit(embed=embed)
