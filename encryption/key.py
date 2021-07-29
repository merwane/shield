from cryptography.fernet import Fernet

class Key:
    def __init__(self, key=""):
        self.key = key

    def generate(self):
        self.key = Fernet.generate_key()
        return self.key

    def save(self):
        with open("shield.key", "wb") as key_file:
            key_file.write(self.key)

    def load(self):
        return open("shield.key", "rb").read()

    def read(self):
        return self.key
