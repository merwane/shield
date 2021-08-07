from api.resources.files.download import get_file_full_path
from flask_restful import Resource
from flask import send_from_directory, request
from services.queue_config import JobQueue
from file_handler.manage import delete_file
from config import FILES_PATH

# job queue
job_queue = JobQueue('default')
queue = job_queue.queue()

class DownloadFile(Resource):
    def get(self, filename):
        # key = request.headers.get('Authorization')
        
        # full_path = get_file_full_path(filename)
        
        filename = send_from_directory(FILES_PATH, filename)
        # queue.enqueue(delete_file, name, result_ttl=0)
        
        return filename 

"""
class DownloadFileEncrypted(Resource):
    def get(self, filename):
        name = download_encrypted(filename)
        tmp_file = send_from_directory('/tmp', filename)
        
        return tmp_file
"""