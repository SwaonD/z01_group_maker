from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE

def get_group_id(msg_id: int) -> int:
	"""Goes through the tables to fetch the group id

	Args:
		msg_id (int): Message ID

	Returns:
		int: Returns the group ID 
	"""
	id = GROUPS_TABLE.get_data(f"{GROUPS_TABLE.message_id} = {msg_id}", GROUP_MEMBERS_TABLE.id)
	return id[0][0]

def get_group_members(group_id: int):
	"""Returns the numbers of members for the same group

	Args:
		group_id (int): Group id
  
	Returns:
		list: All members for the group
	"""
	members = GROUP_MEMBERS_TABLE.get_data(f"{GROUP_MEMBERS_TABLE.group_id} = {group_id}", GROUP_MEMBERS_TABLE.user_id)
	return members

def is_member(group_id: int, user_id: int):
    members = get_group_members(group_id=group_id)
    for m in members:
        if m[0] == user_id:
            return True
    return False