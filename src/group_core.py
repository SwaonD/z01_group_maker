import discord

async def ping(interaction: discord.Interaction, note: str):
	await interaction.response.send_message(f'pong: {note}')

async def createGroup(interaction: discord.Interaction, project_name: str):
    await interaction.response.send_message(f'{interaction.user.mention} wants to create a group for {project_name}')