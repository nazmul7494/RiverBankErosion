from osgeo import gdal
import tkinter
from tkinter import filedialog as fd


# -------------- Function for selecting and getting file path names ------------------------

def selectAndGetFilePaths():

    # Creating the root tkinter object for file selector gui
    root = tkinter.Tk()
    root.withdraw()  # not displaying the root window, only the selection window

    allFilePaths = fd.askopenfiles(parent=root, title='Select All The Image Files to Be Converted: ')

    numOfFilesSelected = len(allFilePaths)

    paths = []  # this list will hold all the absolute file paths of the selected image files

    for i in range(0, numOfFilesSelected):
        paths.append(allFilePaths[i].name)  # Retrieving individual file paths from each ioTextWrapper object
    root.destroy()

    return paths

# ----------------------- Function for Scaling and Saving the Resultant Images ------------------


def ScaleAndSaveSelectedImages(pathNames):

    tgtRes = input("Enter the target resolution: ")
    tgtRes = int(tgtRes)

    root = tkinter.Tk()
    destDir = fd.askdirectory(parent=root, title='Select Directory To Save Images: ')
    print(destDir)
    for i in range(0, len(pathNames)):

        sourceFile = pathNames[i]
        destFile = destDir+"/Converted_Image" + str(i+1) + ".tif"
        gdal.Warp(destFile, sourceFile, xRes=tgtRes, yRes=tgtRes)


file_paths = selectAndGetFilePaths()
ScaleAndSaveSelectedImages(file_paths)

print("Conversion Completed")










