import os
from dotenv import load_dotenv
from dataclasses import dataclass
from src.settings.messages import TextMessages

load_dotenv()

BOT_TOKEN = os.getenv("Z_01_GROUP_MAKER_DISCORD_BOT_TOKEN")

# DIRECTORIES
ROOT_DIR = f"{os.path.dirname(os.path.abspath(__file__))}/../.."
DATA_DIR = f"{ROOT_DIR}/data"
LOG_DIR = f"{ROOT_DIR}/log"

# FILES
GROUP_SQL_FILE_PATH = f"{DATA_DIR}/group_data.db"
PROJECT_NAMES_FILE_PATH = f"{DATA_DIR}/project_names.txt"
GENERAL_LOG_FILE_PATH = f"{LOG_DIR}/general.log"
MSG_LOG_FILE_PATH = f"{LOG_DIR}/msg.log"
SQL_LOG_FILE_PATH = f"{LOG_DIR}/sql_request.log"

# GROUP CONFIGS
LIST_CMD_CONF_GROUP_MAX = 5 # max confirmated groups printed by the list cmd
GROUP_MIN_SIZE = 2
GROUP_MAX_SIZE = 20

# GENERAL CONFIGS
NOTIF_MSG_TIMEOUT = 6

# OTHER
MSG = TextMessages("fr") # msg language


# DEVELOPMENT
LOG_MAX_LINES = 300
DEVS_IDS_STR = os.getenv("Z_01_GROUP_MAKER_DEVS_IDS")
# add the env variable to enable commands for devs
# format: Z_01_GROUP_MAKER_DEVS_IDS=xxxxxxxxxxxxx,xxxxxxxxxxxxx,xxxxxxxxxxxxx


class Variables:
	project_names: list[str] = []
	registered_guilds = set()

@dataclass
class Group:
	id: int
	guild_id: int
	channel_id: int
	message_id: int
	project_name: str
	leader_id: int
	size_limit: int
	description: str
	confirmed: int
