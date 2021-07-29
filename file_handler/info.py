from os import path
from config import FILES_PATH
from file_handler.utils import bytesto
from collections import defaultdict
from math import sqrt
import datetime

class File:
    def __init__(self, filename):
        self.filename = filename
        self.filepath = "{}/{}".format(FILES_PATH, filename)

    def size(self, size_unit="b"):
        file_size = path.getsize(self.filepath)
        if size_unit == "b":
            pass
        else:
            file_size = bytesto(file_size, size_unit)
        return file_size

    def full_path(self):
        return self.filepath

    def file_type(self):
        extension = path.splitext(self.filename)[1]
        extension = extension.replace(".", "")
        return extension

    def last_modified(self):
        last_modified = path.getmtime(self.filepath)
        last_modified = datetime.datetime.fromtimestamp(last_modified)
        return last_modified
