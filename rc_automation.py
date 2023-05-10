import os
from google.cloud import storage
import glob
import pprint
import shutil
import subprocess
import pandas as pd

def get_folder_name():
    storage_client = storage.Client.from_service_account_json(private_key)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob("processdataset.txt")
    folder_to_process = blob.download_as_string()
    
    return folder_to_process.decode("utf-8")

def download_images_from_bucket(folder_name):
    storage_client = storage.Client.from_service_account_json(private_key)
    bucket = storage_client.get_bucket(bucket_name)
    blobs = list(bucket.list_blobs(prefix=folder_name))

    if not os.path.exists(local_script_folder + folder_name):
        os.makedirs(local_script_folder + "/" + folder_name)
        os.makedirs(local_script_folder + folder_name + "/" + dataset)

    if not os.path.exists(local_script_folder + "rc_script" + "/" + "/Images"):
        os.makedirs(local_script_folder + "rc_script" + "/" + "Images")

    for blob in blobs:
        if (not blob.name.endswith("/")):
            blob.download_to_filename(local_script_folder + blob.name)
            print(blob.name + " downloaded from bucket to local folder " + local_script_folder + folder_name + "/" + dataset)
            shutil.move(local_script_folder + blob.name, local_script_folder + "rc_script" + "/" + "Images")
            print(blob.name + " file moved to " + local_script_folder + "Images")

    os.rmdir(local_script_folder + folder_name + "/images")
    os.rmdir(local_script_folder + folder_name)

def run_reality_capture(batchfilepath):
    p = subprocess.Popen(batchfilepath)
    stdout, stderr = p.communicate()

# upload RC assets (fbx and csv) to bucket
def upload_to_bucket(files):
    storage_client = storage.Client.from_service_account_json(private_key)
    bucket = storage_client.get_bucket(bucket_name)
    for filename in files:
        blob = bucket.blob(object_dest_folder + filename)
        blob.upload_from_filename(local_script_folder + "rc_script/" + filename )

def create_virtual_environment():
    main_environment = local_script_folder + "main"
    new_environment_folder = local_script_folder + folder_name + "/VR_environment"
    return shutil.copytree(main_environment, new_environment_folder)

def run_unrealproject(project_path):
    os.startfile(project_path)


private_key = "private_key_file.json"
bucket_name = 'dsd-cloud-storage'
folder_name = get_folder_name()
folder_name = "dji_demo6"
print(folder_name)
local_script_folder = "C://Users/paperspace/Desktop/rc_script/"
dataset = "images"


batchfilepath = local_script_folder + "rc_script" + "/" + "TestScript.bat"
object_dest_folder = folder_name + "/objects/" 

download_images_from_bucket(folder_name)
run_reality_capture(batchfilepath)
#upload_to_bucket(["OfficeScptTest.fbx", "OfficeScptTest_u1_v1_diffuse.png"])
project_path = create_virtual_environment()
print(project_path+ "/MyProject.uproject")
run_unrealproject("C://Users/paperspace/Desktop/rc_script/dji_demo3/VR_environment"+ "/MyProject.uproject")

