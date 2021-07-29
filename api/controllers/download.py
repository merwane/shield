from api.resources.files.download import decrypt_and_download, download_encrypted
from flask_restful import Resource
from flask import send_from_directory, request
from services.queue_config import JobQueue
from file_handler.manage import delete_file

# job queue
job_queue = JobQueue('default')
queue = job_queue.queue()

class DownloadFile(Resource):
    def get(self, filename):
        key = request.headers.get('Authorization')
        name = decrypt_and_download(filename, key)
        
        tmp_file = send_from_directory('/tmp', filename)
        queue.enqueue(delete_file, name, result_ttl=0)
        
        return tmp_file 

class DownloadFileEncrypted(Resource):
    def get(self, filename):
        name = download_encrypted(filename)
        tmp_file = send_from_directory('/tmp', filename)
        
        return tmp_file
