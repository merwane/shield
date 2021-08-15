from config import FILES_PATH
import psutil
import time
import glob
import os

# uptime in hours
def uptime():
    up = time.time() - psutil.boot_time()
    return int(up / 3600)

def cpu_usage():
    usage = psutil.cpu_percent()
    return usage

def memory_usage():
    usage = psutil.virtual_memory()
    return usage

def file_count():
    files = glob.glob("{}/*".format(FILES_PATH))
    file_n = []
    for f in files:
        if os.path.isdir(f):
            pass
        elif f == "{}/swapfile".format(FILES_PATH):
            pass
        else:
            file_n.append(f)

    return len(file_n)