import os
from dotenv import load_dotenv

load_dotenv()

GUILD_ID = 352509375266422797
GROUP_CHANNEL_ID = int(os.getenv("Z_01_GROUP_CHANNEL_ID"))
# commands1 1253719751541264434
# commands 1253698115425533953
GROUP_SQL_FILE = os.getenv("Z_01_GROUP_DB")
LOG_FILE_PATH = os.getenv("Z_01_GROUP_LOG_FILE_PATH")
SQL_LOG_FILE_PATH = os.getenv("Z_01_GROUP_SQL_LOG_FILE_PATH")

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
