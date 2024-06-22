from discord import ui, Interaction
from src.settings.tables import GROUPS_TABLE, GROUP_MEMBERS_TABLE

# SWAON TEST PART
async def test_group_sql(ctx: Interaction, name: str = "Undefined"):
	view = await generate_group_view()
	message = await ctx.channel.send(content=f"project {name}", view=view)
	if message is not None:
		id = GROUPS_TABLE.insert_data(message.id, name, ctx.user.id)
		GROUP_MEMBERS_TABLE.insert_data(id, ctx.user.id)
	ctx.response.is_done()

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
