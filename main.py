from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# methods
from api.controllers.upload import UploadFile
from api.controllers.download import DownloadFile, DownloadFileEncrypted
from api.controllers.files import ListAllFiles, DeleteFile
from api.controllers.device import DiskMonitor, DeviceMonitor
from api.controllers.access import AccessAuthorization, CreatePassword

app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

api.add_resource(UploadFile, "/")
api.add_resource(DownloadFile, "/<string:filename>")
api.add_resource(DownloadFileEncrypted, "/enc/<string:filename>")
api.add_resource(DeleteFile, "/<string:filename>")

api.add_resource(ListAllFiles, "/files")

api.add_resource(DiskMonitor, "/disk")
api.add_resource(DeviceMonitor, "/device")

api.add_resource(AccessAuthorization, "/access")
api.add_resource(CreatePassword, "/password")

if __name__ == '__main__':
    app.run(port=8000)
