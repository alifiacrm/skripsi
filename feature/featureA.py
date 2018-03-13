from scipy import ndimage
import numpy as np

def pixel_count(image):
    count = 0
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[0]):
            if image[i,j] == False:
                count+=1
    return count
# Image Partitioning Approaches
def zoning(image, row, col):
    # Variabel penampung sementara
    label = list()
    feature = list()

    # Image Centroid
    XImageCentroid, YImageCentroid = ndimage.measurements.center_of_mass(image)

    # feature.append(float(str(round(XImageCentroid,2))))
    # feature.append(float(str(round(YImageCentroid,2))))

    feature.append(XImageCentroid)
    feature.append(YImageCentroid)

    TotalRow = int(image.shape[0]/row)
    TotalCol = int(image.shape[1]/col)


    ZoneCentroid = list()     # zone centroid
    XZoneCentroidL = list()
    YZoneCentroidL = list()
    EuclidianImageToZone = list()   # zone euclidian beetwen image centroid and zone centroid
    EuclidianZoneToZone = list()    # zone euclidian each zone to zone
    EuclidianImageToPixel = list()    # Image Centroid to each pixel
    Black = list()
    BlackperBlack = list()
    BlackperWhite = list()
    x1 = 0; y1 = col;

    # Zone Centroid and Distance Zone to Image
    countzti = 0
    for i in range(0, TotalRow):
        x2 = 0; y2 = col;
        for j in range(0, TotalCol):
            XZoneCentroid, YZoneCentroid = ndimage.measurements.center_of_mass(image[x1:y1,x2:y2])
            tmp = np.sum(image[x1:y1,x2:y2])
            tmp = (row*col)-tmp
            Black.append(tmp)

            ZoneToImage = np.sqrt(((XImageCentroid - XZoneCentroid)**2) + ((YImageCentroid - YZoneCentroid)**2))

            ZoneCentroid.append((XZoneCentroid, YZoneCentroid))
            # EuclidianImageToZone.append(ZoneToImage)

            # XZoneCentroidL.append(float(str(round(XZoneCentroid,2))))
            # YZoneCentroidL.append(float(str(round(YZoneCentroid,2))))
            # EuclidianImageToZone.append(float(str(round(ZoneToImage,2))))
            # BlackperWhite.append(float(str(round((tmp/((row*col)-tmp)),2))))

            XZoneCentroidL.append(XZoneCentroid)
            YZoneCentroidL.append(YZoneCentroid)
            EuclidianImageToZone.append(ZoneToImage)
            BlackperWhite.append((tmp/((row*col)-tmp)))

            x2+=row; y2+= col;
            countzti+=1
        x1+=row;y1+=col;
    # print(BlackperWhite)


    # Zone to zone
    countztz = 0
    for i in range(0, (TotalRow*TotalCol)):
        for j in range(i+1, (TotalRow*TotalCol)):
            Zonetozone = (np.sqrt(((ZoneCentroid[i][0] - ZoneCentroid[j][0])**2) + ((ZoneCentroid[i][1] - ZoneCentroid[j][1])**2)))
            EuclidianZoneToZone.append(Zonetozone)

            # Black per black
            if Black[j] == 0:
                tmp = 0
            else:
                tmp = Black[i]/Black[j]
            BlackperBlack.append(tmp)
            countztz+=1

    # Pixel to image
    countitp = 0
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            centroidtopixel = (np.sqrt(((i - XImageCentroid)**2) + ((j - YImageCentroid)**2)))
            EuclidianImageToPixel.append(centroidtopixel)

            # feature.append(float(str(round(centroidtopixel,2))))
            # label.append(str("ITP"+str(i)+str(j)))
            countitp+=1

    feature += XZoneCentroidL
    feature += YZoneCentroidL
    feature += EuclidianImageToZone
    feature += EuclidianZoneToZone
    feature += EuclidianImageToPixel
    feature += BlackperWhite
    feature += BlackperBlack
    # print("Image Centroid : ", Imc)
    # print("Zone Centroid  : ",ZoneCentroid)
    # print("Zone to Image  : ",EuclidianImageToZone)
    # print("Zone to Zone   : ",EuclidianZoneToZone)
    # print("Image to pix   : ",EuclidianImageToPixel)


    # print("countzti : ", countzti)
    # print("countztz : ",countztz)
    # print("countitp : ",countitp)
    # print(len(feature))
    return feature

# Histogram Based Approaches
def projection_histogram(image):
    row = image.shape[0]
    col = image.shape[1]
    vertical = list()
    horizontal = list()

    # Stardart Projection Histogram 2D
    for i in range(row):
        horizontal.append(np.sum(image[i:i+1,0:]))

    for i in range(col):
        vertical.append(np.sum(image[0:,i:i+1]))

    feature = list()
    feature = horizontal + vertical
    # print(len(feature))
    return feature
