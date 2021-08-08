from shutil import copyfile
from config import FILES_PATH
from flask_restful import abort
import os

def get_file_full_path(filename):
    filename = "{}/{}".format(FILES_PATH, filename)
    is_valid = os.path.isfile(filename)
    if is_valid:
        pass
    else:
        abort(404, error="file not found")

    return filename