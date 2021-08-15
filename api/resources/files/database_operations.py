from api.models.unique_file import UniqueFile
from services.database_config import Database
from file_handler.utils import calculate_file_checksum
from config import FILES_PATH

# Database
client = Database()
database = client.light()

def add_file(filename, file_size, file_type, labels):
    filepath = "{}/{}".format(FILES_PATH, filename)
    checksum = calculate_file_checksum(filepath)
    unique_file = UniqueFile(
        filename=filename,
        file_size=file_size,
        file_type=file_type,
        labels=labels,
        checksum=checksum
    )
    unique_file.save()

def add_many(files_data):
    files = []
    for f in files_data:
        filepath = "{}/{}".format(FILES_PATH, f)
        checksum = calculate_file_checksum(filepath)
        files.append(
            UniqueFile(
                filename=f['filename'],
                file_size=f['file_size'],
                file_type=f['file_type'],
                labels=f['labels'],
                checksum=checksum
            )
        )
    
    UniqueFile.objects.insert(files)
    files.save()

def delete_file_from_db(filename):
    database.unique_file.delete_one(
        {"filename": filename}
    )