from PyInquirer import prompt
from cli.upload import upload_file
from cli.download import download_file, delete_file
from cli.access import revoke_access
from config import RESTART_CLI_COMMAND
import time
import os

menu_list = [{
    "type": "list",
    "name": "action",
    "message": "What do you want to do?",
    "choices": ['Upload a file', 'Download a file', 'Delete a file', 'Exit', 'Reload CLI', 'Revoke access']
    }]

def restart_cli(n=3):
    time.sleep(n)
    os.system(RESTART_CLI_COMMAND)

def display():
    menu_list_answer = prompt(menu_list)
    menu_list_answer = menu_list_answer['action']

    if menu_list_answer == 'Upload a file':
        upload_file()
    elif menu_list_answer == 'Download a file':
        download_file()
    elif menu_list_answer == 'Delete a file':
        delete_file()
    elif menu_list_answer == 'Reload CLI':
        restart_cli(0.1)
    elif menu_list_answer == 'Revoke access':
        revoke_access()
    else:
        os.system('clear')
        exit()
