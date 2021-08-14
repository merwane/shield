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

def nuke_everything():
    confirmation_field = [{
        'type': 'confirm',
        'name': 'confirmation',
        'message': 'Are you sure?'
    }]

    confirmation = prompt(confirmation_field)

    if confirmation['confirmation'] == False:
        print('Aborted...')
        print("\n")
        restart()
    else:
        r = api.delete_all_files()
        if r == 200:
            print('Done!')
            print("\n")
            restart()