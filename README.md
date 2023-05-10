# Automation

### Table of Contents
1. [Description](#Description)
3. [Installation](#Installation-Proccess) 
5. [Migration Notes](#Migration-Notes)


## Description
* Overall Description: 
* Photogrammetry Script: The photogrammetry script turns the images taken from the drone into a 3D model by using Reality Capture. It is a .bat file which opens reality capture, aligns images, calculates a model, simplifies the model, calculates the texture, and exports the camera location, the .fbx model, and textures for the .fbx.
* Unreal Import Script
* Unreal Package Script
* Launch VR Environment Script
* RPI-> GC Script 
## Installation
**Prequisites**


**Installation**


## Migration Notes
* Photogrammetry Script
    * The photogrammetry script may need adjustments. We we're operating under the assumption that the EE team would deliver at least 5 data sets by the end of the semester to work out any problems with our script but none were delivered.
    * The script must be placed inside a folder along with files "exportcsv.xml" which holds csv export settings, "exportFBX.xml" which holds FBX export settings, and a folder named "Images" containing the drone images.
    * ![image](https://github.com/disaster-drone/automation/assets/94029910/6f1c4492-16df-4cc2-a35a-9083533e0b9d) Sets the coordinate system. This may need to be updated to whichever coordinate system the dataset was taken in.
    * ![image](https://github.com/disaster-drone/automation/assets/94029910/3cb0662b-d0ed-479d-91e2-47e7d3cfd1c0) Currently, the model is being simplified to 250,000 triangles. If you are looking for more detail, set it higher. Keep in mind this may affect performance within the VR Environment,



* Unreal Import Script
* Unreal Package Script
* Launch VR Environment Script
* RPI-> GC Script 
