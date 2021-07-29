from dotenv import load_dotenv
from os.path import join, dirname
import platform
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

REDIS_HOST = "localhost"
REDIS_PORT = "6379"
REDIS_URI = "redis://{}:{}".format(REDIS_HOST, REDIS_PORT)

RQ_HOST = "localhost"
RQ_PORT = "6379"

# Mac
if platform.system() == "Darwin":
    FILES_PATH = os.getenv('FILES_PATH')
    DISK_PATH = os.getenv('DISK_PATH')
    API_URL = os.getenv("API_URL")
elif platform.system() == "Linux":
    # RPi
    FILES_PATH = "/extdisk"
    DISK_PATH = "/extdisk"
    API_URL = "http://shield.local"

ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
DOWNLOADS_FOLDER = "/Users/merwane/Downloads"
RESTART_CLI_COMMAND = "python shield.py"
