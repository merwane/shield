from services.database_config import Database
from file_handler.utils import datetime_to_string

# Database
client = Database()
database = client.light()

def get_all_files():
    data = []
    all_files = database.unique_file.find({})
    for f in all_files:
        data.append({
            "filename": f['filename'],
            "file_size": f['file_size'],
            "file_type": f['file_type'],
            "added_at": datetime_to_string(f['added_at'])
        })
    
    return data