from cryptography.fernet import Fernet
from config import FILES_PATH

def encrypt_file(filename, key, local=False):
    f = Fernet(key)
    
    if local == False:
        full_path = "{}/{}".format(FILES_PATH, filename)
    else:
        # path to the local file
        full_path = "{}".format(filename)

    with open(full_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    # overwrites file with encrypted file
    with open(full_path, "wb") as file:
        file.write(encrypted_data)
    
    return filename
