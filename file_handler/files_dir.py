import os
import glob
from config import FILES_PATH
from file_handler.info import File
from file_handler.utils import datetime_to_string

def list_files(extension=None, filenames_only=False):
    if extension == None:
        files = glob.glob("{}/*".format(FILES_PATH))
    else:
        files = glob.glob("{}/*.{}".format(FILES_PATH, extension))
    
    if filenames_only == False:
        pass
    else:
        filenames = []
        for path in files:
            basename = os.path.basename(path)
            filenames.append(basename)
        
        files = filenames

    return files

def list_files_with_props():
    files = []
    file_paths = list_files()

    for filepath in file_paths:
        filename = os.path.basename(filepath)
        f = File(filename)
        file_size = f.size('m')
        file_type = f.file_type()
        last_modified = f.last_modified()
        files.append({
            "filename": filename,
            "filepath": filepath,
            "size": file_size,
            "file_type": file_type,
            "last_modified": datetime_to_string(last_modified)
            })

    return files
