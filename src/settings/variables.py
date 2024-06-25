import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

GUILD_ID = 352509375266422797
GROUP_CHANNEL_ID = int(os.getenv("Z_01_GROUP_CHANNEL_ID"))
# commands1 1253719751541264434
# commands 1253698115425533953
GROUP_SQL_FILE = os.getenv("Z_01_GROUP_DB")
LOG_FILE_PATH = os.getenv("Z_01_GROUP_LOG_FILE_PATH")
SQL_LOG_FILE_PATH = os.getenv("Z_01_GROUP_SQL_LOG_FILE_PATH")
NOTIF_MSG_TIMEOUT = 5.0

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

@dataclass
class Group:
	id: int
	message_id: int
	project_name: str
	leader_id: int
	size_limit: int
	description: str
	confirmed: int
