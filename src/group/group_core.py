from discord import ui, Interaction, Embed, Colour, ui, TextStyle
# from src.utils.sql import sql_add_group
# from src.utils.other import is_in_list
from src.settings.variables import PROJECT_NAMES
from src.settings.tables import GROUP_TABLE
import logging

# Modal to ask for project name
class project_modal(ui.Modal, title='Group Creation'):
	project = ui.TextInput(label="What project do you wanna work on ?",
			style=TextStyle.short, placeholder="ascii-art, groupie-tracker...", required=True)

	async def on_submit(self, ctx:Interaction):
		# Check if the project is valid
		if self.project.value not in PROJECT_NAMES:
			await ctx.response.send_message("This project doesn't exists. Try again !")
			return

		embed_desc = f'''
			{ctx.user.mention} created a group for ```{self.project.value}```
		'''
		embed = Embed(
			description=embed_desc,
			title="Group Creation",
			colour=Colour.from_str("#FFF"),
			type="rich"
		)

		embed.add_field(name="Members", value="0", inline=False)
		logging.info(f'{ctx.user} created a group for {self.project}')
		await ctx.response.send_message(embed=embed)

async def create_group(interaction: Interaction):
	await interaction.response.send_modal(project_modal())


# SWAON TEST PART
async def test_group_sql(ctx:Interaction, name:str="Undefined"):
	view = await generate_group_view()
	message = await ctx.channel.send(content=f"project {name}", view=view)
	if message is not None:
		GROUP_TABLE.insert_data(message.id, name, ctx.user.id)
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
