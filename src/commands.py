from discord import Interaction, Object
from typing import Optional
from discord.app_commands import CommandTree
from src.group.commands.create_group import create_group
from src.group.commands.status import status
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
			description="list every groups", guild=Object(id=GUILD_ID))
	async def list_command(ctx: Interaction, name: Optional[str]):
		await list(ctx, name)

	@tree.command(name="status",
			description="Display your infos", guild=Object(id=GUILD_ID))
	async def status_command(ctx: Interaction):
		await status(ctx)

# async def ping(ctx:Interaction):
# 	await ctx.response.send_message("pong")
