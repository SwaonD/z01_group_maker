from discord import Interaction, Embed, Colour
from src.group.message.tools import get_group_members, get_group, Group


async def update_embed(ctx: Interaction):
	group: Group = get_group(ctx.message.id)
	group_members = get_group_members(group.id)

	usernames: str = ""
	for m in group_members:
		usernames += ctx.client.get_user(m[0]).mention
		if m[0] == group.creator_id:
			usernames += " :crown:"
		usernames += "\n"

	msg = ""
	color = ""
	emoji = ""

	if group.confirmed == 1:
		msg = "This group is confirmed !"
		color = "#008000"
		emoji = ":lock: "
	else:
		msg = "Not confirmed yet !"
		color = "#FFF"
		emoji = ":unlock: "

	embed: Embed = Embed(
		description=group.description,
		title=f"{group.project_name}    {len(group_members)}/{group.size_limit}",
		colour=Colour.from_str(color),
		type="rich"
	)

	embed.add_field(name="Members", value=usernames, inline=False)
	embed.add_field(name="Status", value=emoji+msg, inline=False)
	await ctx.message.edit(embed=embed)
