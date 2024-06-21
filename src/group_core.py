import discord

async def ping(interaction: discord.Interaction, note: str):
	print("coucou")
	await interaction.response.send_message(f'pong: {note}')
