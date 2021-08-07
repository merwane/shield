from flask_restful import Resource
from flask import send_from_directory, request
from config import FILES_PATH

class DownloadFile(Resource):
    def get(self):
        filename = request.json['filename']
        filename = send_from_directory(FILES_PATH, filename)
        
        return filename