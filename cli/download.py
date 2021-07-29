from cli.api import ShieldApi
from cli.done import restart
from PyInquirer import prompt

api = ShieldApi()

def download_file():
    name_field = [{
        'type': 'input',
        'name': 'filename',
        'message': 'Enter a file name'
    }]

    filename = prompt(name_field)
    r = api.download_file(filename)
    print("\n")

    if r == 200:
        print('Done!')
        print("\n")
        restart()

def delete_file():
    name_field = [{
        'type': 'input',
        'name': 'filename',
        'message': 'Enter a file name'
    }]

    filename = prompt(name_field)
    r = api.delete_file(filename)
    print("\n")

    if r == 200:
        print('Done!')
        print("\n")
        restart()