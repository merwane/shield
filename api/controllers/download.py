from flask_restful import Resource
from flask import send_from_directory, request
from config import FILES_PATH
from services.queue_config import JobQueue
from file_handler.compress import create_zipfile, delete_zipfile, delete_temp_dir

# job queue
job_queue = JobQueue('default')
queue = job_queue.queue()

class DownloadFile(Resource):
    def get(self):
        filename = request.json['filename']

        if type(filename) == str:
            send_file = send_from_directory(FILES_PATH, filename)
        elif type(filename) == list:
            # Grab filepaths, zip into one file in tmp and send
            zip_filename = create_zipfile(filename)
            zip_filename_ext = "{}.zip".format(zip_filename)
            send_file = send_from_directory("/tmp", zip_filename_ext)
            # queue tmp file deletion
            queue.enqueue(delete_zipfile, zip_filename_ext, result_ttl=0)
            queue.enqueue(delete_temp_dir, zip_filename, result_ttl=0)

        return send_file