from src.settings.variables import PROJECT_NAMES
from src.settings.tables import GROUP_MEMBERS_TABLE, GROUPS_TABLE

def is_project(project: str):
	for p in PROJECT_NAMES:
		if p == project:
			return True
	return False

def project_exists(project: str, author: str):
    group_id = GROUPS_TABLE.get_data(f"{GROUPS_TABLE.project_name} = '{project}' AND {GROUPS_TABLE.creator_id} = '{author}'", GROUPS_TABLE.id)
    if group_id != None:
        return True
    return False