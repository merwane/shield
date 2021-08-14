import os
import glob
from config import FILES_PATH
from file_handler.info import File
from file_handler.utils import datetime_to_string
from api.resources.files.query import get_file_labels

def list_files(extension=None, filenames_only=False):
    if extension == None:
        files = glob.glob("{}/*".format(FILES_PATH))
    else:
        files = glob.glob("{}/*.{}".format(FILES_PATH, extension))
    
    if filenames_only == False:
        filenames = []
        for path in files:
            if os.path.isdir(path):
                pass
            elif path == "{}/swapfile".format(FILES_PATH):
                pass
            else:
                filenames.append(path)
    else:
        filenames = []
        for path in files:
            basename = os.path.basename(path)
            if os.path.isdir(path):
                pass
            else:
                filenames.append(basename)

    return filenames

def list_files_with_props():
    files = []
    file_paths = list_files()

    for filepath in file_paths:
        filename = os.path.basename(filepath)
        f = File(filename)
        file_size = f.size('m')
        file_type = f.file_type()
        last_modified = f.last_modified()

        # get labels
        if file_type in ['png', 'jpg', 'jpeg']:
            labels = get_file_labels(filename)
        else:
            labels = []

        files.append({
            "filename": filename,
            "filepath": filepath,
            "size": file_size,
            "file_type": file_type,
            "labels": labels,
            "last_modified": datetime_to_string(last_modified)
            })

    return files

# lists file in a given directory
def list_files_in_dir(dirpath, extension=None):
    if os.path.isdir(dirpath) == False:
        raise Exception("Not a directory")
    
    if extension == None:
        full_path = "{}/*".format(dirpath)
    else:
        full_path = "{}/*.{}".format(dirpath, extension)

    files = glob.glob(full_path)

    return files