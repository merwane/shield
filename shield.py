from cli import banner, list_files, menu, device_monitor
from cli import access
import os

def main():
    os.system('clear')
    print("\n")
    banner.display()
    print("\n")
    ###
    device_monitor.display()
    print("\n")
    # password check
    # password_check = access.password_check()
    # if password_check == True:
    #    pass

    print("\n")
    list_files.all()
    print("\n")
    menu.display()
    ###
    print("\n")


if __name__ == '__main__':
    main()