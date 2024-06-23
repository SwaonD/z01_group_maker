from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from dataclasses import dataclass


@dataclass
class Group:
    id: int
    message_id: int
    project_name: str
    creator_id: int


def get_group(msg_id: int):
    """Fetches the whole group information using the provided message ID

        Args:
                msg_id (int): Message ID of the group

        Returns:
            Group: Returns the group dataclass

    """

    rows = GROUPS_TABLE.get_data(f"{GROUPS_TABLE.message_id} = {msg_id}", GROUPS_TABLE.id,
                                 GROUPS_TABLE.message_id, GROUPS_TABLE.project_name, GROUPS_TABLE.creator_id)[0]
    group = Group(rows[0], rows[1], rows[2], rows[3])

    return group    


def get_group_id(msg_id: int) -> int:
    """Goes through the tables to fetch the group id

    Args:
            msg_id (int): Message ID

    Returns:
            int: Returns the group ID 
    """
    id = GROUPS_TABLE.get_data(
        f"{GROUPS_TABLE.message_id} = {msg_id}", GROUP_MEMBERS_TABLE.id)
    return id[0][0]


def get_group_members(group_id: int):
    """Returns the numbers of members for the same group

    Args:
            group_id (int): Group id

    Returns:
            list: All members for the group
    """
    members = GROUP_MEMBERS_TABLE.get_data(
        f"{GROUP_MEMBERS_TABLE.group_id} = {group_id}", GROUP_MEMBERS_TABLE.user_id)
    return members


def is_member(group_id: int, user_id: int):
    members = get_group_members(group_id=group_id)
    for m in members:
        if m[0] == user_id:
            return True
    return False
