:: switch off console output
@echo off

:: path to RealityCapture application
set RealityCaptureExe="C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe"

:: root path to work folders where all the datasets are stored (%~dp0 means the flder in which this script is stored)
set RootFolder=%~dp0

:: variable storing path to images for creating model
set Images="%RootFolder%\Images"

:: set a new name for calculated model
set ModelName="OfficeScptTest"

:: set the path, where model is going to be saved, and its name
set Model="%RootFolder%\OfficeScptTest.obj"

:: variable storing path to images for texturing model
set Project="%RootFolder%\OfficeScptTest.rcproj"

:: set a name for image meta data
::set MetaDataFileName = "OfficeScptTestMetaData"

:: set the path, where the image meta data file is going to be saved, and its name
::set MetaDataFile = "%RootFolder%\OfficeScptTestMetaData.csv"

:: run RealityCapture
%RealityCaptureExe% -addFolder %Images% ^
        -align ^
		-setProjectCoordinateSystem epsg:32632 ^
        -setReconstructionRegionAuto ^
        -calculateNormalModel ^
        -selectMarginalTriangles ^
        -removeSelectedTriangles ^
        -renameSelectedModel %ModelName% ^
        -calculateTexture ^
		-cleanModel ^
        -save %Project% ^
        -exportModel %ModelName% %Model% "%~dp0exportsettings.xml"^
		-exportXMP ^
        -quit
       
        

        





