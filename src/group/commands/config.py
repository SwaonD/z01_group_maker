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
	GROUPS_CONFIG.insert_data(ctx.guild_id, group_channel.id)
	await send_quick_response(ctx, \
			MSG.GROUP_CHANNEL_CONFIGURED % (group_channel.mention))
