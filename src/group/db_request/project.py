from src.settings.tables import GROUPS_TABLE
from src.settings.variables import PROJECT_NAMES
from src.utils.log import LOGGER


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


def project_exists(project: str, author_id: int) -> bool:
	"""Verifies in the database if a project was already created by the user

	Args:
		project (str): project name
		author (str): projects's author

	Returns:
		bool: returns True is the project was already found
	"""
	group_id = GROUPS_TABLE.get_data(f"{GROUPS_TABLE.project_name} = \
			'{project}' AND {GROUPS_TABLE.leader_id} = '{author_id}'",
			GROUPS_TABLE.id)
	LOGGER.msg(f"[*] Checked if project {project} already exists :" \
			+ f" {len(group_id) != 0}")
	if len(group_id) != 0:
		return True
	return False
