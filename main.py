# Yang digunakan
import os
import sys
import time

# PraProcessing
from praprocessing import image_resized

# Utility
from utils import progress

# Feature
from feature.featureA import zoning, projection_histogram

from skimage.morphology import skeletonize
from skimage.io import imread
from skimage.util import invert
from skimage.filters import threshold_otsu, sobel_h, sobel_v
from skimage.transform import probabilistic_hough_line
from skimage.feature import corner_peaks
import numpy as np
import matplotlib.pyplot as plt
import csv

#=======| Variabel |========
start_time = time.time()
path_source = "D:/Code/repository/skripsi/dataset/data/"
path_save = "D:/Code/repository/skripsi/dataset/resize/"
# path_source = "D:/Code/repository/skripsi/dataset/test/"
# path_save = "D:/Code/repository/skripsi/dataset/test_resize/"
size = 50
count = 1
zoning_pixel_size = 10
feature = list()

#=======| Resizing Image |========
image_resized(path_source, path_save, size)


dirs = os.listdir(path_save)
numberfiles = len(dirs)
print("")
for item in dirs:
    path = path_save + item
    if os.path.isfile(path):
        image = imread(str(path), as_grey=True)

        otsu = threshold_otsu(image)
        data = image > otsu
        skeleton = skeletonize(data)

        # Zoning
        dzoning = zoning(data, zoning_pixel_size, zoning_pixel_size)

        # Projection Histogram
        dphistogram = projection_histogram(data)

        dt = list()
        # print(str(item.split("_")[0]))
        dt = [str(item.split("_")[0])] + dzoning + dphistogram
        feature.append(dt)
        progress(count, numberfiles, "Feature extraction")
        count += 1


label = list()
label += ['label']
for i in range(len(feature[0])-1):
    label.append("f" + str(i + 1))

print("")
count = 0

with open('data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Label
    datawriter.writerow(label)
    # Value
    for i in range(0, len(feature)):

        myFormattedList = [ '%.2f' % feature[i][j] for j in range(1,len(feature[i])) ]
        tmp = [feature[i][0]] + myFormattedList
        datawriter.writerow(tmp)
        progress(count, len(feature), "Writing data.csv")
        count += 1
    progress(count, len(feature), "Writing data.csv")

print("\nProgram running in %s seconds" % (time.time() - start_time))
# print(len(feature[0]['value']))
# for i in range(0, len(feature)):
# print(i,' : ', len(feature[i]['label']))
#     for j in range(0, len(feature[i]['label'])):
#         print(feature[i]['label'][j],' ',feature[i]['value'][j])
