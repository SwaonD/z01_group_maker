import discord
from discord import ui
from src.utils.project import is_project
import logging

# Modal to ask for project name
class project_modal(ui.Modal, title='Group Creation'):
    project = ui.TextInput(label="What project do you wanna work on ?", style=discord.TextStyle.short, placeholder="ascii-art, groupie-tracker...", required=True)
    
    async def on_submit(self, interaction: discord.Interaction):
        # Check if the project is valid
        if is_project(self.project.value) is False:
                await interaction.response.send_message("This project doesn't exists. Try again !")
                return
            
        embed_desc = f'''
			{interaction.user.mention} created a group for ```{self.project.value}```
		'''
        embed = discord.Embed(
			description=embed_desc,
			title="Group Creation", 
			colour=discord.Colour.from_str("#FFF"), 
			type="rich"
		)
        
        embed.add_field(name="Members", value="0", inline=False)
        logging.info(f'{interaction.user} created a group for {self.project}')
        await interaction.response.send_message(embed=embed)
        
async def create_group(interaction: discord.Interaction):
    await interaction.response.send_modal(project_modal())
    
async def ping(interaction: discord.Interaction, note: str):
	await interaction.response.send_message(f'pong: {note}')