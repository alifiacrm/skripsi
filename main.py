# Yang digunakan
import os
import sys
import time

# PraProcessing
from praprocessing import image_resized

# Utility
from utils import progress

# Feature
from feature.featureA import zoning, zoning_dev

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
# path_source = "D:/Code/skripsi/dataset/data/"
# path_save = "D:/Code/skripsi/dataset/resize/"
path_source = "D:/Code/skripsi/dataset/test/"
path_save = "D:/Code/skripsi/dataset/test_resize/"
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
        dt = zoning(data, zoning_pixel_size, zoning_pixel_size)
        feature.append(dt)
        progress(count, numberfiles, "Feature extraction")
        count += 1

print("")
count=0
with open('data.csv', 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Label
    datawriter.writerow(feature[0]['label'])
    # Value
    for i in range(0, len(feature)):
        datawriter.writerow(feature[i]['value'])
        progress(count, len(feature), "Writing data.csv")
        count += 1
    progress(count, len(feature), "Writing data.csv")

print("\nProgram running in %s seconds" % (time.time() - start_time))

# for i in range(0, len(feature)):
    # print(i,' : ', len(feature[i]['label']))
#     for j in range(0, len(feature[i]['label'])):
#         print(feature[i]['label'][j],' ',feature[i]['value'][j])
