import psutil
import time

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
