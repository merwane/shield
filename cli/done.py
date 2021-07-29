from config import RESTART_CLI_COMMAND
import time
import os

def restart():
    time.sleep(0.5)
    os.system(RESTART_CLI_COMMAND)