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





filepaths = selectAndGetFilePaths()


for i in range(0,imageNum):

    originalImageName = 'E:\\1.ML_Project\\OwnCode\\RiverBankErosion\\OriginalImages\\' + 'B'+str(i+1)+'.tif'
    convImageName = 'E:\\1.ML_Project\\OwnCode\\RiverBankErosion\\ConvertedImages\\'+'B'+str(i+1)+'_Converted.tif'

    # Scaling image using gdal warp function
    gdal.Warp(convImageName, originalImageName, xRes=resInt, yRes=resInt)









