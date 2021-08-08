from flask_restful import Resource, reqparse
from api.resources.files.upload import upload_files
from flask import request
import werkzeug

class UploadFile(Resource):
    def post(self):

        parse = reqparse.RequestParser()
        parse.add_argument('file',
                type=werkzeug.datastructures.FileStorage,
                location="files",
                action='append')
        args = parse.parse_args()
        all_files = args.get('file')

        filenames = upload_files(all_files)

        return filenames