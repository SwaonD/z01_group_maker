from discord import ui, TextStyle, Interaction
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.tools import Group, get_group_members, get_group_id, get_group
from src.utils.log import log


class Confirm(ui.Modal, title='Group deletion'):
	def __init__(self, group: Group, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.group = group
		self.add_item(ui.TextInput(label="Group Name", required=False, default=group.project_name, style=TextStyle.short))

	async def on_submit(self, ctx: Interaction):
		members = get_group_members(self.group.id)
	
		for m in members:
			GROUP_MEMBERS_TABLE.delete_data(
				f"{GROUP_MEMBERS_TABLE.id} = {self.group.id} AND {GROUP_MEMBERS_TABLE.user_id} = {m[0]}")

		GROUPS_TABLE.delete_data(
			f"{GROUPS_TABLE.id} = {get_group_id(self.group.message_id)}")
		await ctx.message.delete()

		log(f"{ctx.user.id} deleted group {self.group.id}", None)
		await ctx.response.send_message(f"{ctx.user.mention} deleted the {self.group.project_name} group", ephemeral=True, delete_after=5.0)