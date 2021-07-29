import shutil
from file_handler.utils import bytesto

class Disk:
    def __init__(self, disk_path):
        self.total, self.used, self.free = shutil.disk_usage(disk_path)

    def total_space(self, unit='g'):
        size = bytesto(self.total, unit)
        return size

    def used_space(self, unit='g'):
        size = bytesto(self.used, unit)
        return size

    def free_space(self, unit='g'):
        size = bytesto(self.free, unit)
        return size

    def disk_space_percentage(self):
        percentages = {}
        space_used_percentage = (self.used * 100) / self.total
        percentages['used'] = float(f'{space_used_percentage:.2f}')
        space_free_percentage = 100 - space_used_percentage
        percentages['free'] = float(f'{space_free_percentage:.2f}')
         
        return percentages
