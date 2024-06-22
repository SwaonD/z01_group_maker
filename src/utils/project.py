from src.settings.variables import PROJECT_NAMES
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE

def is_project(project: str) -> bool:
	"""Verifies if a project is valid

	Args:
		project (str): project name to be checked

	Returns:
		bool: returns True if the project is a valid one
	"""
	for p in PROJECT_NAMES:
		if p == project:
			return True
	return False

def project_exists(project: str, author: str) -> bool:
	"""Verifies in the database if a project was already created by the user

	Args:
		project (str): project name
		author (str): projects's author

	Returns:
		bool: returns True is the project was already found
	"""
	group_id = GROUPS_TABLE.get_data(f"{GROUPS_TABLE.project_name} = '{project}' AND {GROUPS_TABLE.creator_id} = '{author}'", GROUPS_TABLE.id)
	print(group_id)
	print(len(group_id))	
	if len(group_id) != 0:
		return True
	return False
