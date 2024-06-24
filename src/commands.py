from discord import Interaction, Object, User
from typing import Optional
from discord.app_commands import CommandTree, describe
from src.group.commands.create_group import create_group
from src.group.commands.list import list
from src.settings.variables import GUILD_ID

def register_commands(tree: CommandTree):
	# @tree.command(name="ping", description="ping", guild=Object(id=GUILD_ID))
	# async def ping_command(ctx:Interaction):
	# 	await ping(ctx)

	@tree.command(name="create",
			description="Create a group", guild=Object(id=GUILD_ID))
	async def create_command(ctx: Interaction, project: str):
		await create_group(ctx, project)

	@tree.command(name="list",
			description="List every groups", guild=Object(id=GUILD_ID))
	@describe(project_name="Filter by project name",
			user="Filter by user", show_confirmed_group="Show every groups")
	async def list_command(ctx: Interaction, project_name: Optional[str],\
			user: Optional[User], show_confirmed_group: Optional[bool]):
		await list(ctx, project_name, user, show_confirmed_group)

# async def ping(ctx:Interaction):
# 	await ctx.response.send_message("pong")
