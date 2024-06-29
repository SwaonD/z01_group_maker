from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import Group


def get_group(msg_id: int) -> Group | None:
	"""Fetches the whole group information using the provided message ID

																																	Args:
																																																																																																	msg_id (int): Message ID of the group

																																	Returns:
																																																																	Group: Returns the group dataclass

	"""
	group = GROUPS_TABLE.get_groups(f"{GROUPS_TABLE.message_id} = {msg_id}")

	if len(group) == 0:
		return None

	return group[0]


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


def get_group_members_ids(group_id: int) -> list[int]:
	"""Returns the numbers of members for the same group

	Args:
																																																																	group_id (int): Group id

	Returns:
																																																																	list: All members for the group
	"""
	members_data = GROUP_MEMBERS_TABLE.get_data(
		f"{GROUP_MEMBERS_TABLE.group_id} = {group_id}", GROUP_MEMBERS_TABLE.user_id)

	members_ids = []

	for row in members_data:
		members_ids.append(row[0])

	return members_ids


def get_group_msg_id(group_id: int) -> Group:
	group = GROUPS_TABLE.get_groups(
		f"{GROUPS_TABLE.group_id} = {group_id}")
	return group[0]


def get_group_leader_id(msg_id: int) -> int:
	group = get_group(msg_id)
	return group.leader_id


def get_all_groups_leader(leader_id: int) -> list[Group]:
	fetched_groups: list[Group] = GROUPS_TABLE.get_groups(
		f"{GROUPS_TABLE.leader_id} = {str(leader_id)}")

	groups: list[Group] = []
	for g in fetched_groups:
		groups.append(g)
  
	return groups


def is_member(group_id: int, user_id: int) -> bool:
	members_ids = get_group_members_ids(group_id=group_id)

	for id in members_ids:
		if id == user_id:
			return True

	return False


def is_group_leader(group_id: int, user_id: int) -> bool:
	leader_id = get_group_leader_id(get_group_msg_id(group_id))
	
	if leader_id == user_id:
		return True
	
	return False
