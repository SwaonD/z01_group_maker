from discord import Interaction, Object
from typing import Optional
from discord.app_commands import CommandTree
from src.group.commands.create_group import create_group
from src.group.commands.list import list
from src.settings.variables import GUILD_ID

def register_commands(tree: CommandTree):
	@tree.command(name="ping", description="ping", guild=Object(id=GUILD_ID))
	async def ping_command(ctx:Interaction):
		await ping(ctx)

	@tree.command(name="create",
			description="Create a group", guild=Object(id=GUILD_ID))
	async def create_command(ctx: Interaction, project: str):
		await create_group(ctx, project)

	@tree.command(name="list",
			description="list every groups", guild=Object(id=GUILD_ID))
	async def list_command(ctx: Interaction, name: Optional[str]):
		await list(ctx, name)

async def ping(ctx:Interaction):
	await ctx.response.send_message("pong")

# NOTES:
# @tree.command(name="delete_message", description="delete_message", guild=discord.Object(id=GUILD_ID))
# async def delete_message_command(interaction: discord.Interaction, user: Optional[str], all_user: Optional[bool],
# 				channel: Optional[Union[discord.TextChannel, discord.VoiceChannel]]):
# 	await free_server.message_managment(interaction, user, all_user, channel, to_delete=True)
