import discord

async def edit_embed(message, title, description, color, url, embed_index):
	if not embed_index:
		embed_index = 0
	embeds = message.embeds
	if len(embeds) > embed_index:
		# edit the selected embed from the selected message
		myEmbed = embeds[embed_index]
		if title:
			myEmbed.title = title
		if description:
			myEmbed.description = description
		if color:
			myEmbed.color = color
		if url:
			myEmbed.url = url
		await message.edit(embeds=embeds)
	else:
		# new embed into the selected message
		myEmbed = discord.Embed(title=title, description=description, color=color, url=url)
		embeds.append(myEmbed)
		await message.edit(embeds=embeds)

async def embed(interaction, title, description, color, url, message_id, embed_index):
	try:
		if color:
			color = discord.Colour.from_str(color)
		if message_id:
			# edit embed
			message = await interaction.channel.fetch_message(int(message_id))
			await edit_embed(message, title, description, color, url, embed_index)
			await interaction.response.send_message(content="done", ephemeral=True)
		else:
			# new embed
			myEmbed = discord.Embed(title=title, description=description, color=color, url=url)
			await interaction.response.send_message(embed=myEmbed)
	except Exception as e:
		print(e)
		await interaction.response.send_message(content=e, ephemeral=True)

async def remove_embed(interaction, message_id, embed_index):
	try:
		message = await interaction.channel.fetch_message(int(message_id))
		embeds = message.embeds
		if embed_index:
			del embeds[embed_index]
		else:
			embeds = []
		await message.edit(embeds=embeds)
		await interaction.response.send_message(content="done", ephemeral=True)
	except Exception as e:
		print(e)
		await interaction.response.send_message(content=e, ephemeral=True)

# add field and remove field
