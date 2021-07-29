from tabulate import tabulate
from cli.getters import file_list

def all():
    files = file_list.get()
    
    # create a 2D list
    all_files_list = []
    for f in files:
        file_size = round(f['size'], 2)
        all_files_list.append([
            ">",
            f['filename'],
            str(file_size) + " mb",
            f['file_type'],
            f['last_modified']
            ])

    cli_list = tabulate(all_files_list, headers=["#", 'filename', 'size', 'type', 'modified'])
    
    print(cli_list)
