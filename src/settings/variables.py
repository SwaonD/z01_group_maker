import os
from dotenv import load_dotenv
from dataclasses import dataclass
from src.settings.messages import TextMessages

load_dotenv()

BOT_TOKEN = os.getenv("Z_01_GROUP_MAKER_DISCORD_BOT_TOKEN")
ROOT_DIR = f"{os.path.dirname(os.path.abspath(__file__))}/../.."
GROUP_SQL_FILE_PATH = f"{ROOT_DIR}/data/group_data.db"
GENERAL_LOG_FILE_PATH = f"{ROOT_DIR}/log/general.log"
MSG_LOG_FILE_PATH = f"{ROOT_DIR}/log/msg.log"
SQL_LOG_FILE_PATH = f"{ROOT_DIR}/log/sql_request.log"
NOTIF_MSG_TIMEOUT = 6

LIST_CMD_CONF_GROUP_MAX = 5
PROJECT_NAMES = [
	"ascii-art",
	"ascii-art-fs",
	"ascii-art-output",
	"ascii-art-color",
	"ascii-art-web",
	"ascii-art-web-export-file",
	"ascii-art-web-dockerize",
	"ascii-art-web-stylize",
	"groupie-tracker"
]

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
