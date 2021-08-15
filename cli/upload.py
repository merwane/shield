from cli.api import ShieldApi
from cli.done import restart
from PyInquirer import prompt
import os

api = ShieldApi()

def upload_file():
    path_field = [{
        'type': 'input',
        'name': 'file_path',
        'message': 'Enter a file or directory path'
    }]

    classification_field = [{
        'type': 'confirm',
        'name': 'classification_field',
        'message': 'Classify images?'
    }]

    filepath = prompt(path_field)
    if os.path.isdir(filepath['file_path']) == True:
        classification = prompt(classification_field)
        classification = classification['classification_field']
        
        r = api.upload_dir_content(filepath['file_path'], classification=classification)
    else:
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