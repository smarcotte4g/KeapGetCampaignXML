# Make sure Infusionsoft Library is installed
from infusionsoft.library import Infusionsoft
import base64
import os

appname = 'CHANGEME'
api_key = 'CHANGEME'
filebox_id = CHANGEME

infusionsoft = Infusionsoft(appname, api_key)

def get_file():
    file_path = "campaign/"
    os.makedirs(file_path, exist_ok=True)
    with open("campaign/{}-{}.xml".format(appname,filebox_id), "w", encoding="utf-8") as f:
        string = infusionsoft.FileService('getFile', filebox_id)
        f.write(base64.b64decode(string).decode('utf-8'))

def push_file():
    # Change the File Name if necessary
    # with open("file/NEWFILENAMEHERE.xml", "rb") as campaign_file:
    with open("campaign/{}-{}.xml".format(appname,filebox_id), "rb") as campaign_file:
        encoded = base64.b64encode(campaign_file.read()).decode('utf-8')
    stringy = infusionsoft.FileService('replaceFile', filebox_id, encoded)
    print(stringy)

if __name__=="__main__":
    # Comment out the one you are not using so first start with get_file()
    # and after you edit the file # out get_file() and uncomment push_file()
    get_file()
    #push_file()