from discord import ui, Interaction, ButtonStyle, Button, User, Member
from src.group.message.buttons import join_group, leave_group, delete_group, confirm_group
from src.group.message.tools import get_group, Group
from typing import Union



class GroupMessageView(ui.View):
    def __init__(self, project_name, author: Union[User, Member], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project = project_name
        self.author = author

    async def show(self):
        print(self)

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
        await delete_group(ctx, group)



