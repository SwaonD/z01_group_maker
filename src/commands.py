from discord import Interaction, Member, Guild, TextChannel, app_commands
from discord.app_commands import CommandTree, describe
from typing import Optional
from src.group.commands.create_group import create_group
from src.group.commands.list import list_projects
from src.group.commands.config import config
from src.group.commands.kick import kick_project_autocompletion, kick_member


def register_commands(tree: CommandTree, guilds: list[Guild]):
	@tree.command(name="create",
				  description="Create a group", guilds=guilds)
	@describe(project="Project name", limit="Group size limit",
					  description="Description of the group message")
	async def create_command(ctx: Interaction,
							 project: str, limit: int, description: Optional[str]):
		await create_group(ctx, project, limit, description)

	@tree.command(name="list",
				  description="List every groups", guilds=guilds)
	@describe(project="Filter by project name", user="Filter by user",
					  show_all="Show every groups including confirmed ones")
	async def list_command(ctx: Interaction, project: Optional[str],
						   user: Optional[Member], show_all: Optional[bool]):
		await list_projects(ctx, project, user, show_all)

	@tree.command(name="status",
				  description="Display your current groups", guilds=guilds)
	async def status_command(ctx: Interaction):
		await list_projects(ctx, None, ctx.user, True)

	@tree.command(name="config",
				  description="Configure the bot", guilds=guilds)
	async def config_command(ctx: Interaction, group_channel: TextChannel):
		await config(ctx, group_channel)

	@tree.command(name="kick", \
			description="Kick someone from the specified group", guilds=guilds)
	@app_commands.autocomplete(project=kick_project_autocompletion)
	async def kick_command(ctx: Interaction, project: str, member: Member):
		await kick_member(ctx, project=project, member=member)

# async def ping(ctx:Interaction):
# 	await ctx.response.send_message("pong")
