import platform
import os

def is_rpi():
    if platform.system() == "Linux":
        pass
    else:
        print("Host is not a Linux system. Aborting ...\n")
        exit()


def start():
    is_rpi()
    os.system("docker-compose up -d --build")

def stop():
    os.system("docker-compose down")
