// Fill out your copyright notice in the Description page of Project Settings.


#include "MyBlueprintFunctionLibrary.h"
#include <stdio.h>
#include <iostream>

//UFUNCTION(BlueprintCallable, Category = "Sweet|Utilities")
//static TArray<UObject*> DynamicLoadContentFromPath(FString PathFromContentFolder = "VRTemplate/Blueprints/UI/UTA", UClass* AssetClass = nullptr, bool LoadFromSubfolder = false);
//
//TArray<UObject*> DynamicLoadContentFromPath(FString PathFromContentFolder, UClass* AssetClass, bool LoadFromSubfolder)
//{
//	TArray<UObject*> Array;
//	FString RootFolderFullPath = FPaths::ConvertRelativePathToFull(FPaths::GameSourceDir()) + "Content/" + PathFromContentFolder + "/";
//	//Print("RootFolderPath = " + RootFolderFullPath);
//
//	IFileManager& FileManager = IFileManager::Get();
//
//	TArray<FString> Files;
//
//	FString Ext;
//
//	if (LoadFromSubfolder)
//	{
//		if (!Ext.Contains(TEXT("*")))
//		{
//			if (Ext == "")
//			{
//				Ext = "*.*";
//			}
//			else
//			{
//				Ext = (Ext.Left(1) = ".") ? "*" + Ext : "*." + Ext;
//			}
//		}
//
//		FileManager.FindFilesRecursive(Files, *RootFolderFullPath, *Ext, true, false);
//
//	}
//	else
//	{
//		if (!Ext.Contains(TEXT("*")))
//		{
//			if (Ext == "")
//			{
//				Ext = "*.*";
//			}
//			else
//			{
//				Ext = (Ext.Left(1) = ".") ? "*" + Ext : "*." + Ext;
//			}
//		}
//
//		FileManager.FindFilesRecursive(Files, *(RootFolderFullPath + Ext), true, false);
//	}
//
//	for (int32 i = 0; i < Files.Num(); i++)
//	{
//		FString Path;
//		if (LoadFromSubfolder)
//		{
//			int32 LastForwardSlash = Files * .Find("/", ESearchCase::IgnoreCase, ESearchDir::FromEnd);
//			FString File = Files * .RightChop(LastForwardSlash + 1);
//			FString Folder = Files * .RightChop(Files * .Find(PathFromContentFolder, ESearchCase::CaseSensitive, ESearchDir::FromEnd) + PathFromContentFolder.Len());
//			Folder = Folder.LeftChop(File.Len() + 1);
//			File = File.Left(Find.Find(".", ESearchCase::IgnoreCase, ESearchDir::FromEnd));
//			Path = AssetClass->GetFName().ToString() + "'/Game/" + PathFromContentFolder + Folder + "/" + File + "." + File + "'";
//		}
//		else
//		{
//			Path = AssetClass->GetFName().ToString() + "'/Game" + PathFromContentFolder + "/" + Files * .LeftChop(7) + "." + Files * .LeftChop(7) + "'";
//		}
//		UObject* LoadedObj = StaticLoadObject(AssetClass, NULL, *Path);
//
//		Array.Add(LoadedObj);
//	}
//
//	for (int32 i = 0; i < Array.Num(); i++)
//	{
//		if (Array.Num() > 0 && Array* != nullptr)
//		{
//			//Print(Array*->GetFName().ToString());
//		}
//		else
//		{
//			//Print("Array is empty");
//		}
//	}
//
//	return Array;
//}
