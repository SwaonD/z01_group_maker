import discord
from typing import Optional, Union
from discord.app_commands import CommandTree
from src.group_core import ping, createGroup
from src.settings.variables import GUILD_ID

def register_commands(tree: CommandTree):
	@tree.command(name="ping", description="ping", guild=discord.Object(id=GUILD_ID))
	async def ping_command(interaction: discord.Interaction, note: Optional[str]):
		await ping(interaction, note)
  
	@tree.command(name="create", description="Create a group", guild=discord.Object(id=GUILD_ID))
	async def create_command(interaction: discord.Interaction, project_name: str):
		await createGroup(interaction, project_name)

# NOTES:
# @tree.command(name="delete_message", description="delete_message", guild=discord.Object(id=GUILD_ID))
# async def delete_message_command(interaction: discord.Interaction, user: Optional[str], all_user: Optional[bool],
# 				channel: Optional[Union[discord.TextChannel, discord.VoiceChannel]]):
# 	await free_server.message_managment(interaction, user, all_user, channel, to_delete=True)
