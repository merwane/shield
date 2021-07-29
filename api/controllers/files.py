from flask_restful import Resource
from file_handler.files_dir import list_files_with_props
from services.queue_config import JobQueue
from file_handler.manage import delete_file
from config import FILES_PATH

# job queue
job_queue = JobQueue('default')
queue = job_queue.queue()

class ListAllFiles(Resource):
    def get(self):
        all_files = list_files_with_props()

        return all_files

class DeleteFile(Resource):
    def delete(self, filename):
        name = "{}/{}".format(FILES_PATH, filename)
        queue.enqueue(delete_file, name, result_ttl=0)

        return name
