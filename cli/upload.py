from cli.api import ShieldApi
from cli.done import restart
from PyInquirer import prompt

api = ShieldApi()

def upload_file():
    path_field = [{
        'type': 'input',
        'name': 'file_path',
        'message': 'Enter a file path'
    }]

    filepath = prompt(path_field)
    r = api.upload_file(filepath)
    print("\n")

    if r == 200:
        print('Done!')
        print("\n")
        restart()
    else:
        print('An error occured, please retry...')
        print("\n")
        restart()