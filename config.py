from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7306043964"))
SUPPORT_GRP = "LEGITXSUPPORT"
UPDATE_CHNL = "LEGIT_NETWORKS"
OWNER_USERNAME = "BETLUCKERS"
