import requests
from config import API_URL
from requests.exceptions import ConnectionError
from config import ENCRYPTION_KEY, DOWNLOADS_FOLDER
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper
from cli.done import restart
import os
from file_handler.classifier.image_analysis import classify

class ShieldApi:
    def __init__(self, api_url=API_URL):
        self.api_url = api_url
        
    def get(self, resource):
        endpoint = "{}/{}".format(self.api_url, resource)
        try:
            r = requests.get(endpoint)
        except ConnectionError:
            print("Error connecting to the Shield server... \n")
            exit()
        r = r.json()

        return r
    
    def post(self, resource, data={}):
        endpoint = "{}/{}".format(self.api_url, resource)
        try:
            r = requests.post(endpoint, json=data)
        except ConnectionError:
            print("Error connecting to the Shield server... \n")
            exit()
        r = r.json()

        return r

    def upload_file(self, filepath):
        endpoint = "{}/".format(self.api_url)

        filepath = filepath['file_path']
        filepath = filepath.replace(" ", "")

        file_size = os.stat(filepath).st_size

        try:
            with open(filepath, "rb") as f:
                # get file type
                file_extension = os.path.splitext(f.name)[1]
                file_type = file_extension.replace(".", "")

                # check if it's an image
                if file_type in ['png', 'jpg', 'jpeg']:
                    # initialize image classification
                    print("Starting image analysis ...\n")
                    labels = classify(filepath)
                    print("Done.\n")
                else:
                    labels = []

                # add progress bar
                with tqdm(total=file_size, unit="mb", colour='green', unit_scale=True, unit_divisor=1024) as t:
                    wrapped_file = CallbackIOWrapper(t.update, f, "read")
                    endpoint = "{}?labels={}".format(endpoint, labels[0])
                    r = requests.post(endpoint,
                    files={"file": wrapped_file})
        except ConnectionError:
            print("Error connecting to the Shield server... \n")
            exit()

        r = r.status_code

        return r
    
    def download_file(self, filename):
        filename = filename['filename']
        filename = filename.replace(" ", "")

        endpoint = "{}/".format(self.api_url)
        try:
            r = requests.get(endpoint, stream=True, json={'filename': filename})
            total = int(r.headers.get('content-length', 0))
        except ConnectionError:
            print("Error connecting to the Shield server... \n")
            exit()
        
        if r.status_code == 404:
            print("File not found... \n")
            restart()
        
        local_path = "{}/{}".format(DOWNLOADS_FOLDER, filename)
        # add progress bar
        with open(local_path, 'wb') as file, tqdm(
            total=total,
            unit='mb',
            colour='green',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in r.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)

        return r.status_code
    
    def delete_file(self, filename):
        filename = filename['filename']
        filename = filename.replace(" ", "")

        endpoint = "{}/".format(self.api_url)
        try:
            r = requests.delete(endpoint, json={"filename": filename})
        except ConnectionError:
            print("Error connecting to the Shield server... \n")
            exit()
        
        if r.status_code == 404:
            print("File not found... \n")
            restart()
        
        return r.status_code

    def revoke_access(self):
        endpoint = "{}/{}".format(self.api_url, "access")
        try:
            r = requests.delete(endpoint)
        except ConnectionError:
            print("Error connecting to the Shield server... \n")
            exit()

        return r.status_code