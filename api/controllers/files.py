from flask_restful import Resource
from file_handler.files_dir import list_files_with_props
from services.queue_config import JobQueue
from file_handler.manage import delete_file
from api.resources.files.database_operations import delete_file_from_db
from flask import request
from config import FILES_PATH

# job queue
job_queue = JobQueue('default')
queue = job_queue.queue()

class ListAllFiles(Resource):
    def get(self):
        all_files = list_files_with_props()

        return all_files

class DeleteFile(Resource):
    def delete(self):
        filename = request.json['filename']

        if type(filename) == str:
            name = "{}/{}".format(FILES_PATH, filename)
            queue.enqueue(delete_file, name, result_ttl=0)
            # queue database deletion
            queue.enqueue(delete_file_from_db, filename, result_ttl=0)

        elif type(filename) == list:
            for f in filename:
                name = "{}/{}".format(FILES_PATH, f)
                queue.enqueue(delete_file, name, result_ttl=0)
                queue.enqueue(delete_file, f, result_ttl=0)

        return True