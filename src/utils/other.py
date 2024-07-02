from src.utils.log import LOGGER

def fill_list_with_txt_file(path: str):
	try:
		with open(path, 'r') as f:
			project_names = f.read().splitlines()
			return project_names
	except FileNotFoundError:
		LOGGER.msg(f"Error: file {path} not found")
		return []
