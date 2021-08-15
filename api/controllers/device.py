from flask_restful import Resource
from device.disk import Disk
from device import monitor
from config import DISK_PATH

class DiskMonitor(Resource):
    def get(self):
        disk = Disk(DISK_PATH)
    
        monitor = {}
        monitor['total_space'] = disk.total_space()
        monitor['used_space'] = disk.used_space()
        monitor['free_space'] = disk.free_space()
        monitor['disk_percentage'] = disk.disk_space_percentage()

        return monitor


class DeviceMonitor(Resource):
    def get(self):
        res = {}
        res['uptime'] = monitor.uptime()
        res['cpu_usage'] = monitor.cpu_usage()
        res['memory_usage'] = monitor.memory_usage().percent
        res['file_count'] = monitor.file_count()

        return res
