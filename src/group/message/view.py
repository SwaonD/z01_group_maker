from discord import ui, Interaction, ButtonStyle, Button
from src.group.message.buttons import join_group, leave_group, \
		delete_group_from_button, confirm_group
from src.group.db_request.group import get_group
from src.settings.variables import Group

class GroupMessageView(ui.View):
	def __init__(self):
		super().__init__(timeout=None)

	@ui.button(label="Join", style=ButtonStyle.primary)
	async def join_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		await join_group(ctx, group)

	@ui.button(label="Leave", style=ButtonStyle.secondary)
	async def leave_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		await leave_group(ctx, group)

	@ui.button(label="Confirm", style=ButtonStyle.success)
	async def lock_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		await confirm_group(ctx, group)

	@ui.button(label="Delete", style=ButtonStyle.danger)
	async def delete_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		await delete_group_from_button(ctx, group)
