from cli.progress import print_static_progress_bar
from cli.getters import disk_monitor, device_monitor

def check_disk():
    disk_data = disk_monitor.get()
    used_space = disk_data['used_space']
    used_space = round(used_space, 2)
    used_space = str(used_space)
    used_space = "{} GB".format(used_space)

    used_space_percentage = disk_data['disk_percentage']['used']
    # display
    print_static_progress_bar("Disk  ", used_space_percentage, used_space, "green")

def check_device():
    # device data
    device_data = device_monitor.get()
    uptime = device_data['uptime']
    cpu_usage = device_data['cpu_usage']
    memory_usage = device_data['memory_usage']
    # display
    print_static_progress_bar("CPU   ", cpu_usage, "", "blue")
    print_static_progress_bar("Memory", memory_usage, "", "red")
    print("")
    print("Uptime: {} hours".format(uptime))

def display():
    # disk data
    check_disk()
    # device data
    check_device()
