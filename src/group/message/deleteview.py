import os
from src.utils.log import log
from dotenv import load_dotenv
from discord import ui, Interaction, ButtonStyle, Button
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.group.message.tools import Group, get_group_members, get_group_id

load_dotenv()

class DeleteMessageView(ui.View):
    def __init__(self, group: Group, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group = group

    async def show(self):
        print(self)

    @ui.button(label="Cancel", style=ButtonStyle.primary)
    async def cancel_button_callback(self, ctx: Interaction, button: Button):
        ctx.message.delete()

    @ui.button(label="Delete", style=ButtonStyle.danger)
    async def confirm_delete_button_callback(self, ctx: Interaction, button: Button):
        members = get_group_members(self.group.id)

        for m in members:
            GROUP_MEMBERS_TABLE.delete_data(
                f"{GROUP_MEMBERS_TABLE.id} = {self.group.id} AND {GROUP_MEMBERS_TABLE.user_id} = {m[0]}")

        GROUPS_TABLE.delete_data(
            f"{GROUPS_TABLE.id} = {get_group_id(self.group.message_id)}")
        msg = await ctx.channel.fetch_message(self.group.message_id)
        await msg.delete()
        await ctx.message.delete()

        log(f"{ctx.user.id} deleted group {self.group.id}", None)
        await ctx.response.send_message(f"{ctx.user.mention} deleted the {self.group.project_name} group", ephemeral=True, delete_after=5.0)