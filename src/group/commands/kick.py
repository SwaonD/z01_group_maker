from discord import Interaction, app_commands, Member
from typing import List
from src.group.db_request.group import get_all_groups_leader, get_group, is_member, get_group_leader_id
from src.settings.variables import Group
from src.settings.tables import GROUP_MEMBERS_TABLE
from src.utils.log import log
from src.settings.variables import MSG_LOG_FILE_PATH, MSG, Group
from src.utils.discord import send_quick_response
from src.group.message.core import update_embed


async def kick_project_autocompletion(ctx: Interaction, current: str) -> List[app_commands.Choice[str]]:
    projects = [
        app_commands.Choice(
            name=group.project_name,
            value=str(group.message_id)
        )
        for group in get_all_groups_leader(ctx.user.id)
        if current in group.project_name or current == ""
    ]
    return projects[:20]


async def kick_member(ctx: Interaction, project: str, member: Member):
    group: Group = get_group(int(project))
    member_id: int = member.id
    leader_id: int = get_group_leader_id(group.message_id)

    if is_member(group.id, member_id) is False:
        await send_quick_response(ctx, MSG.NOT_IN_GROUP)
        return

    if leader_id != ctx.user.id:
        await send_quick_response(ctx, MSG.NOT_LEADER)
        return

    if leader_id == member_id:
        await send_quick_response(ctx, MSG.CANT_KICK_LEADER)
        return

    GROUP_MEMBERS_TABLE.delete_data(
        f"{GROUP_MEMBERS_TABLE.group_id} = {group.id} AND"
        + f" {GROUP_MEMBERS_TABLE.user_id} = {member_id}")
    log(f"{ctx.user} left group {group.id}", MSG_LOG_FILE_PATH)

    m = ctx.client.get_user(member_id)
    if m is None:
        m = ctx.client.fetch_user(member_id)

    channel = ctx.guild.get_channel(group.channel_id)
    msg = channel.get_partial_message(group.message_id)

    await m.send(MSG.MEMBER_KICKED_PM % (ctx.user.mention, msg.jump_url))

    await update_embed(ctx, group.message_id)
    await send_quick_response(ctx, MSG.MEMBER_KICKED_CHANNEL % (ctx.user.mention, m.mention, msg.jump_url))
