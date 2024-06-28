from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE
from src.settings.variables import Group

def get_group(msg_id: int):
	"""Fetches the whole group information using the provided message ID

		Args:
				msg_id (int): Message ID of the group

		Returns:
			Group: Returns the group dataclass

	"""
	rows = GROUPS_TABLE.get_data(
			f"{GROUPS_TABLE.message_id} = {msg_id}", GROUPS_TABLE.id,
			GROUPS_TABLE.message_id, GROUPS_TABLE.project_name,
			GROUPS_TABLE.leader_id, GROUPS_TABLE.size_limit,
			GROUPS_TABLE.description, GROUPS_TABLE.confirmed)[0]
	group = Group(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6])

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


def is_member(group_id: int, user_id: int):
	members_ids = get_group_members_ids(group_id=group_id)
	for id in members_ids:
		if id == user_id:
			return True
	return False
