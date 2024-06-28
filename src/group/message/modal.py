from discord import ui, TextStyle, Interaction
from src.group.db_request.group import get_group_members_ids
from src.group.message.core import delete_group
from src.utils.discord import send_quick_response
from src.settings.variables import MSG, Group

class ConfirmDeleteGroup(ui.Modal):
	def __init__(self, group: Group, title: str, *args, **kwargs):
		super().__init__(title=title, *args, **kwargs)
		self.group = group
		self.add_item(ui.TextInput(label="Group Name", required=False,
				default=group.project_name, style=TextStyle.short))

	async def on_submit(self, ctx: Interaction):
		members_ids = get_group_members_ids(self.group.id)
		await delete_group(ctx, self.group, members_ids)
		await send_quick_response(ctx,
			MSG.DELETE_GROUP % (self.group.project_name))
