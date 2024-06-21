from discord import ui, Interaction, PartialEmoji
from src.utils.sql import sql_add_group

async def ping(interaction: Interaction, note:str=""):
	view = await generate_group_view()
	message = await interaction.response.send_message(content=f"pong {note}", view=view)
	await sql_add_group(message.id, interaction.user.id)


async def button_callback(interaction: Interaction):
	await interaction.response.send_message("la mort te regarde")

async def generate_group_view() -> ui.View:
	join_button = ui.Button(label="Rejoindre")
	leave_button = ui.Button(label="Quitter")
	edit_button = ui.Button(label="Editer")
		# style=discord.ButtonStyle.primary
	join_button.callback = button_callback
	new_view = ui.View(timeout=None)
	new_view.add_item(join_button)
	new_view.add_item(leave_button)
	new_view.add_item(edit_button)
	return new_view
