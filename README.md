# Automation

### Table of Contents
1. [Description](#Description)
3. [Installation](#Installation) 
5. [Migration Notes](#Migration-Notes)


## Description
The creation of the VR environment has been automated with a combination of Python, Bash Scripting, and C++. The automation will export an executable VR environment that can be accessed directly through a VR headset like Quest 2. The automation part for this project has multiple components to it and can also be run individually to export the 3D model with textures only as well as creating a VR environment from an existing 3D model (*supported format: .fbx*). 

The following components of the automation are described below:

* Photogrammetry Script: The photogrammetry script turns the images taken from the drone into a 3D model by using Reality Capture. It is a .bat file which opens reality capture, aligns images, calculates a model, simplifies the model, calculates the texture, and exports the camera location, the .fbx model, and textures for the .fbx.
* Unreal Import Script: The Unreal Engine Automation script utilizes the [Unreal Engine Python API](https://docs.unrealengine.com/4.27/en-US/PythonAPI/) and automates importing the images, 3D object and textures, and csv files for image GPS data. Additionally, it also creates a static mesh from the imported objects and creates a datatable using the pre-loaded struct for camera grab feature to work within the VR environment. It outputs a Unreal VR Project ready to be exported.
* Unreal Package Script: The Unreal Package Script is a batch file that exports the previously created Unreal Project to an executable. Currently, the script packages a Windows executable only. 

## Installation
**Prequisites**
- Download Unreal Engine Editor Version: 5.0.3-20979098+++UE5+Release-5.0
- Install [Reality Capture](https://www.capturingreality.com/) Photogrammetry Software
- S3 Object Storage on Google Cloud
- Active [Service Account](https://cloud.google.com/iam/docs/service-accounts-create) with private key downloaded as JSON
- Desktop PC or Virtual Machine with [CUDA-enabled](https://developer.nvidia.com/cuda-gpus) GPU *(See the machine type we used below)*
- Download the install latest [CUDA toolkit](https://developer.nvidia.com/cuda-downloads) for your CPU architecture and OS version

**Machine Type**

Our project has been developed and tested on following machines.


| Machine Name | Operating System | GPU | Processor | RAM | Hard Disk |
| --- | --- | --- | --- | --- | --- |
| Google Cloud Compute Engine | Windows Server 2022 | 1 x NVIDIA T4 Virtual Workstation | n1-highcpu-32 (32 vCPU) | 28.8 GB | 250 GB SSD |
| Paperspace GPU VM | Windows Server 2022 | NVIDIA Quadro RTX4000 | Intel Xeon Silver 4215R (8 vCPU) | 30 GB | 250 GB SSD |
| Desktop PC | Windows 10 | NVIDIA GeForce RTX 2080Ti | AMD Ryzen Threadripper 3960X (24 vCPU) | 16 GB | 1 TB SSD |

> Please note that the actual specifications of your machines may vary. Only NVIDIA GPU support the latest CUDA toolkit

**Installation**

- Clone the repository

   ```
   $ git clone https://github.com/disaster-drone/automation.git
   ```
- Navigate to [private_key_file.json](private_key_file.json) and update the following with your Service Account private key

   ``` JSON
   {
      "type": "service_account",
      "project_id": "",
      "private_key_id": "",
      "private_key": "",
      "client_email": "",
      "client_id": "",
      "auth_uri": "",
      "token_uri": "",
      "auth_provider_x509_cert_url": "",
      "client_x509_cert_url": ""
   }
   ```

## Migration Notes
* Photogrammetry Script
    * The photogrammetry script may need adjustments. We we're operating under the assumption that the EE team would deliver at least 5 data sets by the end of the semester to work out any problems with our script but none were delivered.
    * The script must be placed inside a folder along with files "exportcsv.xml" which holds csv export settings, "exportFBX.xml" which holds FBX export settings, and a folder named "Images" containing the drone images.
    * ![image](https://github.com/disaster-drone/automation/assets/94029910/6f1c4492-16df-4cc2-a35a-9083533e0b9d) Sets the coordinate system. This may need to be updated to whichever coordinate system the dataset was taken in.
    * ![image](https://github.com/disaster-drone/automation/assets/94029910/3cb0662b-d0ed-479d-91e2-47e7d3cfd1c0) Currently, the model is being simplified to 250,000 triangles. If you are looking for more detail, set it higher. Keep in mind this may affect performance within the VR Environment,

* Unreal Import Script
    * The script utilizes Python >= 3.7 and Google Cloud Storage API client library. Use the following command to install the library using pip. 
      
      ```
      pip install --upgrade google-cloud-storage
      ```
      
    * Navigate to [rc_automation.py](rc_automation.py) and update the following directory path with your locally cloned folder and S3 bucket name
      
      ``` Python
      local_script_folder = "C://Users/paperspace/Desktop/rc_script/"
      ```
      ``` Python
      bucket_name = 'dsd-cloud-storage'
      ```

* Unreal Package Script
    * The package script runs a [batch file](ue5packagescript.bat) with necessary configuration settings in the Unreal Project and outputs an executable VR environment.
    * This script assumes Unreal Engine 5.0 is installed in its default location. You can change the path for Unreal Engine in the script if it's installed anywhere else by updating the following line:
      ``` bat
      set UE5_DIR=""
      ```
