from cryptography.fernet import Fernet
from config import FILES_PATH

def decrypt_file(filename, key, tmp=False, local=False):
    f = Fernet(key)
    
    if local == False:
        full_path = "{}/{}".format(FILES_PATH, filename) 
    else:
        # path to the local file
        full_path = "{}".format(filename)
    
    with open(full_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    if tmp == False:
        # overwrites with the original decrypted file
        with open(full_path, "wb") as file:
            file.write(decrypted_data)
    else:
        if local != False:
            raise Exception("Can't have both tmp and local set")
        # send decrypted file to a temporary location
        with open("/tmp/{}".format(filename), "wb") as file:
            file.write(decrypted_data)
    
    if local == False:
        new_path = "/tmp/{}".format(filename)
    else:
        new_path = "{}".format(filename)

    return new_path
