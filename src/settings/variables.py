import os
from dotenv import load_dotenv
from dataclasses import dataclass
from src.settings.messages import TextMessages

load_dotenv()

GROUP_CHANNEL_ID = int(os.getenv("Z_01_GROUP_CHANNEL_ID"))
# commands1 1253719751541264434
# commands 1253698115425533953
GROUP_SQL_FILE = "./data/group_data.db"
GENERAL_LOG_FILE_PATH = "./log/general.log"
MSG_LOG_FILE_PATH = "./log/msg.log"
SQL_LOG_FILE_PATH = "./log/sql_request.log"
NOTIF_MSG_TIMEOUT = 5.0

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
	message_id: int
	project_name: str
	leader_id: int
	size_limit: int
	description: str
	confirmed: int
