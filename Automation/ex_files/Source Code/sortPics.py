import os
from pathlib import Path
from collections import Counter

SUBDIRECTORIES = {
    "jpeg": ['.jpg','.jpeg'],
    "RAW":['.CR2','.CR3','.dng'],
}

jpegList = []
rawList = []

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC' #If filetype doesn't exist in our dictionary


def createFileList(path,emptyList):
    for item in os.scandir(path):
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        name = item.name
        if filetype in name:
            new_name = name.replace(filetype,'')
        print(new_name)
        emptyList.append(new_name)


def deleteFile(rawPath,rawList,jpegList):
    res = list((Counter(rawList) - Counter(jpegList)).elements()) 
    for item in os.scandir(rawPath):
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        name = item.name
        if filetype in name:
            new_name = name.replace(filetype,'')
        if new_name in res:
            print(new_name)
    

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

#organizeDirectory()

jpegPath = input("Enter jpeg path\n")
createFileList(path, jpegList)
rawPath = input("Enter raw path\n")
createFileList(path, rawList)
print(rawList)
print(jpegList)
deleteFile(rawPath,rawList,jpegList)

