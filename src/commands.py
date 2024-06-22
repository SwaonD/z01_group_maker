from discord import Interaction, Object
# from typing import Optional, Union
from discord.app_commands import CommandTree
from src.group.group_core import create_group
from src.group.group_test import test_group_sql
from src.group.group_utils import search
from src.settings.variables import GUILD_ID

def register_commands(tree: CommandTree):
	@tree.command(name="ping", description="ping", guild=Object(id=GUILD_ID))
	async def ping_command(ctx:Interaction):
		await ping(ctx)

	@tree.command(name="create",
			description="Create a group", guild=Object(id=GUILD_ID))
	async def create_command(ctx: Interaction):
		await create_group(ctx)

	@tree.command(name="test_group_sql",
			description="test_group_sql", guild=Object(id=GUILD_ID))
	async def test_group_sql_command(ctx: Interaction, name: str):
		await test_group_sql(ctx, name)

	@tree.command(name="search",
			description="search", guild=Object(id=GUILD_ID))
	async def search_command(ctx: Interaction, name: str):
		await search(ctx, name)

async def ping(ctx:Interaction):
	await ctx.response.send_message("pong")

# NOTES:
# @tree.command(name="delete_message", description="delete_message", guild=discord.Object(id=GUILD_ID))
# async def delete_message_command(interaction: discord.Interaction, user: Optional[str], all_user: Optional[bool],
# 				channel: Optional[Union[discord.TextChannel, discord.VoiceChannel]]):
# 	await free_server.message_managment(interaction, user, all_user, channel, to_delete=True)
