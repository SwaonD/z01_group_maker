from discord import Interaction, TextChannel
from src.settings.tables import GROUPS_CONFIG
from src.settings.variables import MSG
from src.utils.discord import send_quick_response

# SELECT CHANNEL EXAMPLE
# class SettingsView(ui.View):
# 	def __init__(self):
# 		super().__init__()
# 		self.add_item(ChannelSelect())

# class ChannelSelect(ui.ChannelSelect):
# 	def __init__(self):
# 		super().__init__(
# 			placeholder="Select a channel...",
# 			channel_types=[ChannelType.text]
# 		)

# 	async def callback(self, ctx: Interaction):
# 		await set_group_channel(ctx, self)

# async def set_group_channel(ctx: Interaction, select: ui.ChannelSelect):
# 	await send_quick_response(ctx, select.values[0])

async def config(ctx: Interaction, group_channel: TextChannel):
	if ctx.permissions.administrator is False:
		await send_quick_response(ctx, MSG.GROUP_CHANNEL_CONFIG_NOT_AUTHORIZED)
		return
	config_data = GROUPS_CONFIG.get_data(
			f"{GROUPS_CONFIG.guild_id} = {ctx.guild.id}")
	if len(config_data) == 0:
		GROUPS_CONFIG.insert_data(ctx.guild_id, group_channel.id)
	else:
		GROUPS_CONFIG.update_data({GROUPS_CONFIG.group_channel_id: \
				group_channel.id}, f"{GROUPS_CONFIG.guild_id} = {ctx.guild.id}")
	await send_quick_response(ctx, \
				MSG.GROUP_CHANNEL_CONFIGURED % (group_channel.mention))
