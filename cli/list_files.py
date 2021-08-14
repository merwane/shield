from tabulate import tabulate
from cli.getters import file_list

def all():
    files = file_list.get()
    
    # create a 2D list
    all_files_list = []
    for f in files:
        file_size = round(f['size'], 2)
        if f['labels'] == ['']:
            labels = 0
        else:
            labels = f['labels']
        all_files_list.append([
            ">",
            f['filename'],
            str(file_size) + " mb",
            f['type'],
            labels,
            f['last_modified']
            ])

    cli_list = tabulate(all_files_list, headers=["#", 'filename', 'size', 'type', 'labels', 'modified'])
    
    print(cli_list)
