from werkzeug.security import generate_password_hash, check_password_hash
from config import OPERATING_SYSTEM
import os

class ShieldPassword:
    def __init__(self):
        self.password_hash = ""
        # check if password hash file exists
        if OPERATING_SYSTEM == "Linux":
            is_file = os.path.isfile("/keys/hashed_password.key")
        else:
            is_file = os.path.isfile("./hashed_password.key")
        self.is_file = is_file

        if is_file:
            if OPERATING_SYSTEM == "Linux":
                self.password_hash = open("/keys/hashed_password.key", "rb").read()
            else:
                self.password_hash = open("./hashed_password.key", "rb").read()
        else:
            pass

    def write_new_password(self, password):
        self.password_hash = generate_password_hash(password)

        return self.password_hash

    def save_password(self):
        if OPERATING_SYSTEM == "Linux":
            with open("/keys/hashed_password.key", "wb") as password_file:
                    password_hash = self.password_hash.encode()
                    password_file.write(password_hash)
        else:
            with open("./hashed_password.key", "wb") as password_file:
                    password_hash = self.password_hash.encode()
                    password_file.write(password_hash)

    def check_password(self, password):
        hash_match = check_password_hash(self.password_hash.decode("utf-8"), password)

        return hash_match

    def read_password_hash(self):
        return self.password_hash

    def password_exists(self):
        return self.is_file