import requests
import os
import sys
import urllib3

class RequestFile:
    def __init__(self, dir="", filename="", url=""):
        self.dir = dir
        self.filename = filename
        self.url = url
    
    ## --> check if the directory exists
    def check_dir_exists(self):
        if not os.path.exists(self.filepath):
            os.makedirs(self.filepath)

    ## --> create full filename
    def generate_filename(self):
        return self.dir + "/" + self.filename

    ## --> return the full filepath of the file
    def return_filepath(self):
        self.filepath = self.generate_filename()
        return self.filepath

    def download_file(self):
        r = requests.get(self.url, stream = True)

        with open(self.filepath, "wb") as fileDownload:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    fileDownload.write(chunk)
        
        return "Success"