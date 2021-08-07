from zipfile import ZipFile
from config import FILES_PATH
from shutil import copyfile, rmtree
import time
import os

def create_zipfile(files):
    timestamp = str(int(time.time()))
    tmp_location = "/tmp"

    zip_location = '{}/{}.zip'.format(tmp_location, timestamp)

    # create tmp dir with all files
    os.mkdir("/tmp/{}".format(timestamp))
    for f in files:
        copyfile("{}/{}".format(FILES_PATH, f), "/tmp/{}/{}".format(timestamp, f))

    with ZipFile(zip_location, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk("/tmp/{}".format(timestamp)):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, os.path.basename(filePath))

    return timestamp

def delete_zipfile(zipfilename):
    zipfilename = "/tmp/{}".format(zipfilename)
    os.remove(zipfilename)

def delete_temp_dir(tempdirname):
    tempdirname = "/tmp/{}".format(tempdirname)
    rmtree(tempdirname)