from encryption.decrypt import decrypt_file
from shutil import copyfile
from config import FILES_PATH
from flask_restful import abort

def decrypt_and_download(filename, key):
    # copy file to temporary folder
    try:
        copyfile("{}/{}".format(FILES_PATH, filename), "/tmp/{}".format(filename))
    except FileNotFoundError:
        abort(404, error="file not found") 

    # decrypt copied file
    name = decrypt_file(filename, key, tmp=True)

    return name

def download_encrypted(filename):
    try:
        copyfile("{}/{}".format(FILES_PATH, filename), "/tmp/{}".format(filename))
    except FileNotFoundError:
        abort(404, error="file not found")

    return filename
