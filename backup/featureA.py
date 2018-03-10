from scipy import ndimage
import numpy as np

def zoning(image, row, col):
    # Variabel penampung sementara
    label = list()
    value = list()

    # Image Centroid
    XImageCentroid, YImageCentroid = ndimage.measurements.center_of_mass(image)

    value.append(float(str(round(XImageCentroid,2))))
    label.append(str("XIC"))
    value.append(float(str(round(YImageCentroid,2))))
    label.append(str("YIC"))

    TotalRow = int(image.shape[0]/row)
    TotalCol = int(image.shape[1]/col)


    ZoneCentroid = list()     # zone centroid
    EuclidianImageToZone = list()   # zone euclidian beetwen image centroid and zone centroid
    EuclidianZoneToZone = list()    # zone euclidian each zone to zone
    EuclidianImageToPixel = list()    # Image Centroid to each pixel
    x1 = 0; y1 = col;

    # Zone Centroid and Distance Zone to Image
    countzti = 0
    for i in range(0, TotalRow):
        x2 = 0; y2 = col;
        for j in range(0, TotalCol):
            XZoneCentroid, YZoneCentroid = ndimage.measurements.center_of_mass(image[x1:y1,x2:y2])
            ZoneToImage = np.sqrt(((XImageCentroid - XZoneCentroid)**2) + ((YImageCentroid - YZoneCentroid)**2))

            ZoneCentroid.append((XZoneCentroid, YZoneCentroid))
            # EuclidianImageToZone.append(ZoneToImage)

            value.append(float(str(round(XZoneCentroid,2))))
            label.append(str("XZC"+str(i)))
            value.append(float(str(round(YZoneCentroid,2))))
            label.append(str("YZC"+str(i)))
            value.append(float(str(round(ZoneToImage,2))))
            label.append(str("ZTI"+str(i)))
            x2+=row; y2+= col;
            countzti+=1
        x1+=row;y1+=col;

    # Zone to zone
    countztz = 0
    for i in range(0, (TotalRow*TotalCol)):
        for j in range(i+1, (TotalRow*TotalCol)):
            Zonetozone = (np.sqrt(((ZoneCentroid[i][0] - ZoneCentroid[j][0])**2) + ((ZoneCentroid[i][1] - ZoneCentroid[j][1])**2)))
            # EuclidianZoneToZone.append(Zonetozone)

            value.append(float(str(round(Zonetozone,2))))
            label.append(str("ZTZ"+str(i)+str(j)))
            countztz+=1
    countitp = 0
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            centroidtopixel = (np.sqrt(((i - XImageCentroid)**2) + ((j - YImageCentroid)**2)))
            # EuclidianImageToPixel.append(centroidtopixel)

            value.append(float(str(round(centroidtopixel,2))))
            label.append(str("ITP"+str(i)+str(j)))
            countitp+=1

    # print("Image Centroid : ", Imc)
    # print("Zone Centroid  : ",ZoneCentroid)
    # print("Zone to Image  : ",EuclidianImageToZone)
    # print("Zone to Zone   : ",EuclidianZoneToZone)
    # print("Image to pix   : ",EuclidianImageToPixel)
    feature = dict()
    feature['label'] = label
    feature['value'] = value
    # print("countzt1 : ", countzti)
    # print("countztz : ",countztz)
    # print("countitp : ",countitp)
    return feature

#counting the number of black pixel
def zoning_dev(image, type=None, size=None):
    if type == 1:
        # Ukuran Pixel
        # print ("Type 1")
        imagepixel = int(image.shape[0] * image.shape[1])
        zonepixel = int(size * size)
        zone = int(imagepixel / zonepixel)

        x = 0
        y = size
        zonevalue = list()
        for i in range (0, int(image.shape[0]/size)):
            #horizontal
            value = 0
            count = 1
            for j in range (0, image.shape[1]):
                # ini apanya
                for k in range(x, y):
                    if image[k,j] == True:
                        value+=1
                        # print(value)
                if count != size:
                    count+=1
                else:
                    zonevalue.append((value))
                    count = 1
                    value = 0
            x+=size
            y+=size
        print(zonevalue)

    elif type == 2:
        # Jumlah Zone
        print ("type 2")
        print(image.shape[0])
        print(image.shape[1])
    else:
        print ("Type should be added : pixel size (1) or zone sum (2)")
