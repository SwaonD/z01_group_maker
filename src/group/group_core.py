from discord import ui, Interaction, Embed, Colour, ButtonStyle, Button, User, Member, TextChannel
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import GROUP_CHANNEL_ID
from src.utils.project import is_project, project_exists
from src.utils.group import get_group_id, get_group_members, is_member
from src.utils.log import log
import discord
from typing import Union

class MyView(ui.View):
	def __init__(self, project_name, author: Union[User, Member], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.project = project_name
		self.author = author
	async def show(self):
		print(self)

	@ui.button(label="Join", style=ButtonStyle.primary)
	async def callback1(self, ctx: Interaction, button: Button):
		# id = get_group_id(self.msg_id)
		id = get_group_id(ctx.message.id)

		if is_member(id, ctx.user.id):
			await ctx.response.send_message(":x: You are already in this group !", ephemeral=True)
			return

		GROUP_MEMBERS_TABLE.insert_data(id, ctx.user.id)

		await update_members_count(ctx, self.project, self.author)
		await ctx.response.send_message(f"{ctx.user.mention} joined {self.author.mention}'s group for {self.project}", ephemeral=True)

	@ui.button(label="Leave", style=ButtonStyle.secondary)
	async def callback2(self, ctx: Interaction, button: Button):
		id = get_group_id(ctx.message.id)

		if is_member(id, ctx.user.id) is False:
			await ctx.response.send_message(":x: You are not in this group !", ephemeral=True)
			return

		GROUP_MEMBERS_TABLE.delete_data(f"{GROUP_MEMBERS_TABLE.id} = {id} AND {GROUP_MEMBERS_TABLE.user_id} = {ctx.user.id}")

		await update_members_count(ctx, self.project, self.author)
		await ctx.response.send_message(f"{ctx.user.mention} left {self.author.mention}'s group for {self.project}", ephemeral=True)

async def update_members_count(ctx: Interaction, project: str, author: Union[User, Member]):
	group_members = get_group_members(ctx.message.id)

	if len(group_members) == 0:
		GROUPS_TABLE.delete_data(f"{GROUPS_TABLE.id} = {get_group_id(ctx.message.id)}")
		channel: TextChannel = await ctx.client.fetch_channel(GROUP_CHANNEL_ID)
		message = await channel.fetch_message(ctx.message.id)
		await message.delete()
		return

	embed_desc: str = f'''
	{author.mention} created a group for ```{project}```
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

	@ui.button(label="Delete", style=ButtonStyle.danger)
	async def delete_callback(self, ctx: Interaction, button: Button):
		await delete_group(ctx)

async def update_members_count(ctx: Interaction, embed_id: int, embed):
	try:
		# Fetch the partial message by its ID
		channel = ctx.message.guild.get_channel(GROUP_CHANNEL_ID)
		if channel is None:
			channel = await ctx.message.guild.fetch_channel(GROUP_CHANNEL_ID)
		message = channel.get_partial_message(embed_id)
		if message is None:
			message = await channel.fetch_message(embed_id)

		# Edit the message with the new embed
		await message.edit(embed=embed)
	except discord.NotFound:
		print(f"Message with ID {ctx.message.id} not found.")
	except discord.Forbidden:
		print("Bot does not have permissions to edit messages.")
	except discord.HTTPException as e:
		print(f"HTTP error occurred: {e}")


async def create_group(ctx: Interaction, project: str):
	# Checks
	if is_project(project) is False:
		await ctx.response.send_message(":x: This project doesn't exist !")
		return

	if  project_exists(project, ctx.user.id) is True:
		await ctx.response.send_message(":x: You already created a group for this project !")
		return

	# Create the embed
	embed_desc = f'''
	{ctx.user.mention} created a group for ```{project}```
	'''
	embed = Embed(
		description=embed_desc,
		title="Group Creation",
		colour=Colour.from_str("#FFF"),
		type="rich"
	)

	embed.add_field(name="Members", value=ctx.user.mention, inline=False)
	log(f'{ctx.user} created a group for {project}', False)

	v = MyView(project, ctx.user)

	# Send the embed and get the message object
	message = await ctx.response.send_message(embed=embed, view=v)
	message = await ctx.original_response()

 	# Add Group to GROUPDB and Author to the members database
	GROUPS_TABLE.insert_data(message.id, project, ctx.user.id)
	GROUP_MEMBERS_TABLE.insert_data(get_group_id(message.id), ctx.user.id)

	await message.edit(view=v)

async def delete_group(ctx: Interaction):
	await ctx.response.send_message("delete")
