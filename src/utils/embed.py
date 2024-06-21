from discord import Colour, Embed, Interaction

async def edit_embed(message:str, title:str,
		description:str, color:str, url:str, embed_index:int):
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
		myEmbed = Embed(title=title,
				description=description, color=color, url=url)
		embeds.append(myEmbed)
		await message.edit(embeds=embeds)

async def embed(ctx:Interaction, title:str, description:str, color:str=None,
		url:str=None, message_id:str=None, embed_index:int=None):
	try:
		if color:
			color = Colour.from_str(color)
		if message_id:
			# edit embed
			message = await ctx.channel.fetch_message(int(message_id))
			await edit_embed(message, title, description, color, url, embed_index)
			await ctx.response.send_message(content="done", ephemeral=True)
		else:
			# new embed
			myEmbed = Embed(title=title, description=description, color=color, url=url)
			await ctx.response.send_message(embed=myEmbed)
	except Exception as e:
		print(e)
		await ctx.response.send_message(content=e, ephemeral=True)

async def remove_embed(ctx:Interaction, message_id:str, embed_index:int):
	try:
		message = await ctx.channel.fetch_message(int(message_id))
		embeds = message.embeds
		if embed_index:
			del embeds[embed_index]
		else:
			embeds = []
		await message.edit(embeds=embeds)
		await ctx.response.send_message(content="done", ephemeral=True)
	except Exception as e:
		print(e)
		await ctx.response.send_message(content=e, ephemeral=True)

# add field and remove field
