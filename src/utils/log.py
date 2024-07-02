from datetime import datetime
from src.settings.variables import MSG_LOG_FILE_PATH, \
		 SQL_LOG_FILE_PATH, GENERAL_LOG_FILE_PATH, LOG_MAX_LINES

class LogFile():
	def __init__(self, path: str, is_printable: bool):
		self.path = path
		self.is_printable = is_printable

class Logger():
	def __init__(self):
		self.msg_log_file = LogFile(MSG_LOG_FILE_PATH, True)
		self.sql_log_file = LogFile(SQL_LOG_FILE_PATH, False)

	def log(self, text: str, *log_files: LogFile):
		current_datetime = datetime.now()
		date = current_datetime.date()
		time = f"{str(current_datetime.hour)}:{str(current_datetime.minute)}"
		all_log_files = list(log_files)
		all_log_files.append(LogFile(GENERAL_LOG_FILE_PATH, False))
		for log_file in all_log_files:
			try:
				with open(log_file.path, "r") as f:
					lines = f.readlines()
				if len(lines) >= LOG_MAX_LINES:
					lines = lines[(len(lines)-LOG_MAX_LINES+1):]
				log_text = f"{str(date)} {str(time)} | {text}"
				if log_file.is_printable:
					print(log_text)
				lines.append(f"{log_text}\n")
				with open(log_file.path, "w") as f:
					f.writelines(lines)
			except FileNotFoundError:
				print(f"FileNotFoundError: The file '{log_file.path}'" \
						+ " could not be found.")
			except PermissionError:
				print(f"PermissionError: Permission denied when" \
						+ f" trying to access '{log_file.path}'.")
			except Exception as e:
				print(f"An error occurred: {str(e)}")

	def msg(self, text: str):
		self.log(text, self.msg_log_file)

	def sql(self, text: str):
		self.log(text, self.sql_log_file)

LOGGER = Logger()
