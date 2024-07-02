import os
from dotenv import load_dotenv
from dataclasses import dataclass
from src.settings.messages import TextMessages

load_dotenv()

class Variables:
	BOT_TOKEN = os.getenv("Z_01_GROUP_MAKER_DISCORD_BOT_TOKEN")
	ROOT_DIR = f"{os.path.dirname(os.path.abspath(__file__))}/../.."
	DATA_DIR = f"{ROOT_DIR}/data"
	LOG_DIR = f"{ROOT_DIR}/log"

	GROUP_SQL_FILE_PATH = f"{DATA_DIR}/group_data.db"
	PROJECT_NAMES_FILE_PATH = f"{DATA_DIR}/project_names.txt"
	GENERAL_LOG_FILE_PATH = f"{LOG_DIR}/general.log"
	MSG_LOG_FILE_PATH = f"{LOG_DIR}/msg.log"
	SQL_LOG_FILE_PATH = f"{LOG_DIR}/sql_request.log"
	NOTIF_MSG_TIMEOUT = 6

	LIST_CMD_CONF_GROUP_MAX = 5
	PROJECT_NAMES = []

	LOG_MAX_LINES = 300

MSG = TextMessages("fr") # msg language

@dataclass
class Group:
	id: int
	channel_id: int
	message_id: int
	project_name: str
	leader_id: int
	size_limit: int
	description: str
	confirmed: int
