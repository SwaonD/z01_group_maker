from discord import ui, Interaction, Message, PartialEmoji
from src.utils.sql import sql_add_group

async def ping(interaction: Interaction):
	await interaction.response.send_message("pong")


# swaon part
async def test_group_sql(interaction:Interaction, name:str="Undefined"):
	view = await generate_group_view()
	message = await interaction.channel.send(content=f"project {name}", view=view)
	if message is not None:
		await sql_add_group(message.id, name, interaction.user.id)
	interaction.response.is_done()

async def button_callback(interaction: Interaction):
	await interaction.response.send_message("la mort te regarde")

async def generate_group_view() -> ui.View:
	join_button = ui.Button(label="Rejoindre")
	leave_button = ui.Button(label="Quitter")
	edit_button = ui.Button(label="Editer")
		# style=discord.ButtonStyle.primary
	join_button.callback = button_callback
	leave_button.callback = button_callback
	edit_button.callback = button_callback
	new_view = ui.View(timeout=None)
	new_view.add_item(join_button)
	new_view.add_item(leave_button)
	new_view.add_item(edit_button)
	return new_view
