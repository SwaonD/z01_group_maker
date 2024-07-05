from discord import ui, Interaction, ButtonStyle, Button
from src.group.message.buttons import join_group, leave_group, \
		delete_group_from_button, confirm_group
from src.group.db_request.group import get_group
from src.settings.variables import Group

class GroupMessageView(ui.View):
	def __init__(self):
		super().__init__(timeout=None)

	@ui.button(label="Join", style=ButtonStyle.primary, custom_id="join_button")
	async def join_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		if group:
			await join_group(ctx, group)

	@ui.button(label="Leave", style=ButtonStyle.secondary, custom_id="leave_button")
	async def leave_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		if group:
			await leave_group(ctx, group)

	@ui.button(label="Confirm", style=ButtonStyle.success, custom_id="confirm_button")
	async def lock_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		if group:
			await confirm_group(ctx, group)

	@ui.button(label="Delete", style=ButtonStyle.danger, custom_id="delete_button")
	async def delete_button_callback(self, ctx: Interaction, button: Button):
		group: Group = get_group(ctx.message.id)
		if group:
			await delete_group_from_button(ctx, group)
