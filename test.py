# size = 6
# zoning = 2
# x = 0
# y = zoning
# vertical
#
# for i in range (0, int(size/zoning)):
#     #horizontal
#     count = 1
#     for j in range (0, size):
#         # ini apanya
#         for k in range(x, y):
#             print (j,k)
#         if count != zoning:
#             count+=1
#         else:
#             print("---")
#             count = 1
#     print("===")
#     x+=zoning
#     y+=zoning

#
# 01 23 45
# 01 01 01
#
# 01 23 45
# 23 23 23
#
# 01 23 45
# 45 45 45

import numpy as np
# A = np.array(
#     [[1, 0, 0, 0],
#      [0, 0, 1, 1],
#      [0, 1, 1, 1],
#      [1, 1, 1, 1]]
# )
# # A = np.array(
# #     [[1,2,3,4],
# #     [5,6,7,8],
# #     [9,10,11,12],
# #     [13,14,15,16]]
# #     )
# # A = np.array(
# #     [
# #     [1,2,3,4,5,6],
# #     [7,8,9,10,11,12],
# #     [13,14,15,16,17,18],
# #     [19,20,21,22,23,24],
# #     ]
# #     )
# print(A)
# print("----")
# # B = A[0:2,0:2]
# # C = A[0:2,0:2].copy()
# # A[0,1] = 99
# size_row = 2
# size_col = 2
# # print(int(A.shape[1]/size))
# # print(A[0:2,0:2])
# # print(A[0:2,2:4])
# # print(A[0:2,4:6])
# # print("-")
# # print(A[2:4,0:2])
# # print(A[2:4,2:4])
# # print(A[2:4,4:6])
#
# shape0 = int(A.shape[0] / size_row)
# shape1 = int(A.shape[1] / size_col)
# print(shape0, "-", shape1)
# avrg = list()
# x1 = 0
# y1 = size_col
# for i in range(0, shape0):
#     x2 = 0
#     y2 = size_col
#     for j in range(0, shape1):
#         avrg.append(np.average(A[x1:y1, x2:y2]))
#         x2 += size_row
#         y2 += size_col
#     # print("-")
#     x1 += size_row
#     y1 += size_col
# print(avrg)
#
#
# # print(A)
# # print(B)
# # print(C)
#
# size = 2
# imagepixel = int(A.shape[0] * A.shape[1])
# zonepixel = int(size * size)
# zone = int(imagepixel / zonepixel)
#
# x = 0
# y = size
# zonevalue = list()
# for i in range(0, int(A.shape[0] / size)):
#     # horizontal
#     value = 0
#     count = 1
#     for j in range(0, A.shape[1]):
#         for k in range(x, y):
#             # print(k,j,A[k,j])
#             if A[k, j] == 1:
#                 value += 1
#                 # print(value)
#         if count != size:
#             count += 1
#         else:
#             zonevalue.append((value))
#             count = 1
#             value = 0
#             # print("--")
#     x += size
#     y += size
# print(zonevalue)

B = np.array(
    [[1, 2, 3, 3],
     [0, 8, 0, 0],
     [0, 0, 3, 0],
     [1, 0, 2, 1]]
)

print(np.sum(B[0:1,0:]))
print(np.sum(B[1:2,0:]))
print(np.sum(B[2:3,0:]))
print(np.sum(B[3:4,0:]))
print(np.sum(B[0:,0:1]))
print(np.sum(B[0:,1:2]))
print(np.sum(B[0:,2:3]))
print(np.sum(B[0:,3:4]))

B = np.array(
    [[1, 2, 3, 3],
     [1, 0, 2, 1]]
)

print("---")
for i in range(B.shape[0]):
    print (i)

from scipy import ndimage
# Konstanta
# size_row = 2
# size_col = 2
# label = list()
# result = list()
# Xim_c, Yim_c = ndimage.measurements.center_of_mass(B)
#
# result.append(float(str(round(Xim_c, 2))))
# label.append(str("Ximc"))
# result.append(float(str(round(Yim_c, 2))))
# label.append(str("Yimc"))
# Image Centroid

# Imc = ndimage.measurements.center_of_mass(B)
# Calculate Centroid each zone
# Sr = int(B.shape[0] / size_row)
# Sc = int(B.shape[1] / size_col)
# print(shape0,"-",shape1)
# Zc = list()     # zone centroid
# Zeuc = list()   # zone euclidian beetwen image centroid and zone centroid
# Zez = list()    # zone euclidian each zone to zone
# Cep = list()    # Image Centroid to each pixel
# x1 = 0
# y1 = size_col
# for i in range(0, Sr):
#     x2 = 0
#     y2 = size_col
#     for j in range(0, Sc):
#         Xc, Yc = ndimage.measurements.center_of_mass(B[x1:y1, x2:y2])
#         Zonetoimage = np.sqrt(((Xim_c - Xc)**2) + ((Yim_c - Yc)**2))
#
#         Zc.append((Xc, Yc))
#         Zeuc.append(Zonetoimage)
#
#         result.append(float(str(round(Xc, 2))))
#         label.append(str("Zc" + str(i+1)))
#         result.append(float(str(round(Yc, 2))))
#         label.append(str("Yc" + str(i+1)))
#         result.append(float(str(round(Zonetoimage, 2))))
#         label.append(str("Zti" + str(i+1)))
#         x2 += size_row
#         y2 += size_col
    # print("-")
    # x1 += size_row
    # y1 += size_col
# Zone to zone
# for i in range(0, (Sr * Sc)):
#     for j in range(i + 1, (Sr * Sc)):
#         Zonetozone = (
#             np.sqrt(((Zc[i][0] - Zc[j][0])**2) + ((Zc[i][1] - Zc[j][1])**2)))
#         Zez.append(Zonetozone)
#         result.append(float(str(round(Zonetozone, 2))))
#         label.append(str("Ztz" + str(i+1) + str(j+1)))
        # Zc[]
# Image centroid to pixel
# count = 1
# for i in range(0, B.shape[0]):
#     for j in range(0, B.shape[1]):
#         centroidtopixel = (np.sqrt(((i - Xim_c)**2) + ((j - Yim_c)**2)))
#         Cep.append(centroidtopixel)
#         result.append(float(str(round(centroidtopixel, 2))))
#         label.append(str("Ctp" + str(count)))
#         count+=1
# print("Image Centroid : ", Imc)
# print("Zone Centroid  : ",Zc)
# print("Zone to Image  : ",Zeuc)
# print("Zone to Zone   : ",Zez)
# print("Image to pix   : ",Cep)
# feature = dict()
# feature['label'] = label
# feature['value'] = result
# feature['valuex'] = Zc + Zeuc + Zez + Cep
#
# for i in range(0, len(feature['label'])):
#     print(feature['label'][i], " : ", feature['value'][i])
# for i in range(len(feature['valuex'])):
#     print(feature['valuex'][i])
