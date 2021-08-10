from services.database_config import Database
from file_handler.utils import datetime_to_string
from config import FILES_PATH

# Database
client = Database()
database = client.light()

# TODO: do more work here

def get_all_files(full_path=False, file_type=None, labels=None):
    data = []
    query = {}

    # filter file type
    if file_type == None:
        pass
    elif file_type == 'image':
        query = {"file_type": {'$in': ['png', 'jpg', 'jpeg']}}
    elif file_type == 'video':
        query = {"file_type": {'$in': ['mp4']}}
    else:
        pass

    # filter labels
    if labels != None:
        query['labels'] = labels

    all_files = database.unique_file.find(query)
    for f in all_files:
        if full_path == True:
            filename = "{}/{}".format(FILES_PATH, f['filename'])
        else:
            filename = f['filename']
        data.append({
            "filename": filename,
            "file_size": f['file_size'],
            "file_type": f['file_type'],
            "added_at": datetime_to_string(f['added_at'])
        })
    
    return data