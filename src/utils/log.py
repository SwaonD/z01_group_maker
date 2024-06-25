from datetime import datetime
from src.settings.variables import LOG_MAX_LINES, GENERAL_LOG_FILE_PATH

def log(msg: str, *file_paths: str):
	"""This function logs a message to the given file(s)

	Args:
			msg (str): Message to write in the file
			*file_paths (str): Path to the file(s) where the log will be writen
	"""
	current_datetime = datetime.now()
	date = current_datetime.date()
	time = str(current_datetime.hour)+":"+str(current_datetime.minute)
	all_file_paths = list(file_paths)
	all_file_paths.append(GENERAL_LOG_FILE_PATH)
	for file_path in all_file_paths:
		try:
			with open(file_path, "r") as f:
				lines = f.readlines()
			if len(lines) >= LOG_MAX_LINES:
				lines = lines[(len(lines)-LOG_MAX_LINES+1):]
			lines.append(f"{str(date)} | {str(time)} {msg}\n")
			with open(file_path, "w") as f:
				f.writelines(lines)
		except FileNotFoundError:
			print(f"FileNotFoundError: The file '{file_path}' could not be found.")
		except PermissionError:
			print(f"PermissionError: Permission denied when"
		 			+ f" trying to access '{file_path}'.")
		except Exception as e:
			print(f"An error occurred: {str(e)}")
