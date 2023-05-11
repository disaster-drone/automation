import os
from google.cloud import storage
import glob
import pprint
import shutil
import subprocess

def upload_images_to_gcs():
    storage_client = storage.Client.from_service_account_json("private_key_file.json")
    bucket = storage_client.get_bucket('dsd-cloud-storage')
    local_directory_path = os.path.join(os.getcwd(), 'uta' , 'images')
    destination_prefix = 'uta' + '/images'
    print(local_directory_path)
    print(destination_prefix)
    

    for root, dirs, files in os.walk(local_directory_path):
        for file in files:
            # Set the path to the local file
            local_file_path = os.path.join(root, file)

            # Set the destination path for the uploaded file
            destination_blob_name = os.path.join(destination_prefix, os.path.relpath(local_file_path, local_directory_path))

            # Get a reference to the destination blob in the bucket
            blob = bucket.blob(destination_blob_name)

            # Upload the file to the bucket
            blob.upload_from_filename(local_file_path)

upload_images_to_gcs()