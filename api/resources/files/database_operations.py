from api.models.unique_file import UniqueFile
from services.database_config import Database

# Database
client = Database()
database = client.light()

def add_file(filename, file_size, file_type):
    unique_file = UniqueFile(
        filename=filename,
        file_size=file_size,
        file_type=file_type
    )
    unique_file.save()

def add_many(files_data):
    files = []
    for f in files_data:
        files.append(
            UniqueFile(
                filename=f['filename'],
                file_size=f['file_size'],
                file_type=f['file_type']
            )
        )
    
    UniqueFile.objects.insert(files)
    files.save()

def delete_file_from_db(filename):
    database.unique_file.delete_one(
        {"filename": filename}
    )