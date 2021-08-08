from flask_restful import Resource, reqparse
from encryption.encrypt import encrypt_file
from services.queue_config import JobQueue
from config import FILES_PATH
from api.resources.files.database_operations import add_file
from api.resources.files.disk_operations import write_file_on_disk
from flask import request
import werkzeug
import uuid
import os

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

            # Write file to disk
            f.save("{}/{}".format(FILES_PATH, filename))

            # Add file to Files database
            file_type = file_extension.replace(".", "")
            queue.enqueue(add_file, filename, 0, file_type, result_ttl=0)

            filenames.append(filename)

        return filenames