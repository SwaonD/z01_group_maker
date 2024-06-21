import discord
from typing import Optional, Union
from discord.app_commands import CommandTree
from src.group.group_core import ping, test_group_sql
from src.settings.variables import GUILD_ID

def register_commands(tree: CommandTree):
	@tree.command(name="ping", description="ping", guild=discord.Object(id=GUILD_ID))
	async def ping_command(interaction: discord.Interaction):
		await ping(interaction)

	@tree.command(name="test_group_sql",
			description="test_group_sql", guild=discord.Object(id=GUILD_ID))
	async def test_group_sql_command(interaction: discord.Interaction, name:str):
		await test_group_sql(interaction, name)

# NOTES:
# @tree.command(name="delete_message", description="delete_message", guild=discord.Object(id=GUILD_ID))
# async def delete_message_command(interaction: discord.Interaction, user: Optional[str], all_user: Optional[bool],
# 				channel: Optional[Union[discord.TextChannel, discord.VoiceChannel]]):
# 	await free_server.message_managment(interaction, user, all_user, channel, to_delete=True)
