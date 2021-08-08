from flask_restful import Resource, reqparse
from encryption.encrypt import encrypt_file
from services.queue_config import JobQueue
from config import FILES_PATH
from api.resources.files.database_operations import add_file
from file_handler.info import File
from flask import request
import werkzeug
import uuid
import os
from file_handler.utils import bytesto

# job queue
job_queue = JobQueue('default')
queue = job_queue.queue()

class UploadFile(Resource):
    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('file',
                type=werkzeug.datastructures.FileStorage,
                location="files",
                action='append')
        args = parse.parse_args()
        all_files = args.get('file')
        filenames = []
        for f in all_files:
            file_extension = os.path.splitext(f.filename)[1]
            file_uid = uuid.uuid4().hex
            filename = "{}{}".format(file_uid, file_extension)
            file_path = "{}/{}".format(FILES_PATH, filename)

            # Write file to disk
            f.save(file_path)
            
            # get file size
            file_size = os.path.getsize(file_path)
            file_size = bytesto(file_size, 'm')

            # Add file to Files database
            file_type = file_extension.replace(".", "")
            queue.enqueue(add_file, filename, file_size, file_type, result_ttl=0)

            filenames.append(filename)

        return filenames