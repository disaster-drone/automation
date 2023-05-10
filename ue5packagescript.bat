@echo off

setlocal

:: Specify the path to the Unreal Engine installation
set UE5_DIR="D:\UE_5.0"
:: set UE5_PATH="D:\UE_5.0\Engine\Binaries\Win64\UnrealEditor.exe"

:: Specify the path to your project's .uproject file
set PROJECT_PATH="D:\GitHub\VR-Environment\MyProject.uproject"

:: Specify the name of the output executable
set OUTPUT_NAME="MyProject.exe"
  
:: Build the game using the "Development" configuration
%UE5_DIR%\Engine\Build\BatchFiles\RunUAT.bat BuildCookRun ^
   -project="%PROJECT_PATH%" ^
   -noP4 -clientconfig=Development -serverconfig=Development ^
   -nocompileeditor -utf8output -platform=Win64 ^
   -targetplatform=Win64 ^
   -cook -build -stage -pak -archive ^
   -archivedirectory="D:\GitHub\VR-Environment\Executable" ^
   -package ^
   -executable="%OUTPUT_NAME%" ^
   -clean

endlocal