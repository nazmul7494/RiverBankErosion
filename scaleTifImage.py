from osgeo import gdal

numb = input("Enter the number of images to scale: ")
imageNum = int(numb)

resolution = input("Enter the target resolution (i.e.: 30 or 90, etc.): ")
resInt = int(resolution);

# Scaling images from 30m (default) resolution to 90m resolution:

for i in range(0,imageNum):

    originalImageName = 'E:\\1.ML_Project\\OwnCode\\RiverBankErosion\\OriginalImages\\' + 'B'+str(i+1)+'.tif'
    convImageName = 'E:\\1.ML_Project\\OwnCode\\RiverBankErosion\\ConvertedImages\\'+'B'+str(i+1)+'_Converted.tif'

    # Scaling image using gdal warp function
    gdal.Warp(convImageName, originalImageName, xRes=resInt, yRes=resInt)

print("----------------------------------------- Conversion Complete -----------------------------------------------------")







