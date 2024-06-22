from discord import ui, Interaction, Embed, Colour, TextStyle
from src.settings.variables import PROJECT_NAMES
import logging

# Modal to ask for project name
class project_modal(ui.Modal, title = 'Group Creation'):
	project = ui.TextInput(label="What project do you wanna work on ?",
			style=TextStyle.short, placeholder="ascii-art, groupie-tracker...", required=True)

	async def on_submit(self, ctx: Interaction):
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
