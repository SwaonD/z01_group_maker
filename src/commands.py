from discord import Interaction, Member, Guild
from discord.app_commands import CommandTree, describe
from typing import Optional
from src.group.commands.create_group import create_group
from src.group.commands.list import list_projects

# register commands for all known guilds, but only at startup !
def register_commands(tree: CommandTree, guilds: list[Guild]):
	# @tree.command(name="ping", description="ping", guild=Object(id=GUILD_ID))
	# async def ping_command(ctx:Interaction):
	# 	await ping(ctx)

	@tree.command(name="create",
			description="Create a group", guilds=guilds)
	@describe(project="Project name", limit="Group size limit", \
			description="Description of the group message")
	async def create_command(ctx: Interaction,
			project: str, limit: int, description: Optional[str]):
		await create_group(ctx, project, limit, description)

	@tree.command(name="list",
			description="List every groups", guilds=guilds)
	@describe(project="Filter by project name", user="Filter by user",
			show_all="Show every groups including confirmed ones")
	async def list_command(ctx: Interaction, project: Optional[str],\
			user: Optional[Member], show_all: Optional[bool]):
		await list_projects(ctx, project, user, show_all)

	@tree.command(name="status",
			description="Display your current groups", guilds=guilds)
	async def status_command(ctx: Interaction):
		await list_projects(ctx, None, ctx.user, True)

# async def ping(ctx:Interaction):
# 	await ctx.response.send_message("pong")
