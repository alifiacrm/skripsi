import sys, os
from PIL import Image
from numpy import *

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('\r[%s] %s%s | %s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def clearing_files(path):
    dirs = os.listdir(path)
    for item in dirs:
        if os.path.isfile(path+item):
            os.remove(path+item)

def crop_image(data_to_crop):
    cropped_data = []
    for z in xrange(data_to_crop.shape[0]):
        img = data_to_crop[z]
        img = img.reshape(data_to_crop.shape[0], data_to_crop.shape[1])
        rx = -1
        upy = -1
        lx = -1
        by = -1
        for x in xrange(data_to_crop.shape[0]):
            for y in xrange(data_to_crop.shape[1]):
                px = img[x, y]
                if px > 0:
                    if rx == -1 or x > rx:
                        rx = x
                    if lx == -1 or x < lx:
                        lx = x
                    if upy == -1 or y > upy:
                        upy = y
                    if by == -1 or y < by:
                        by = y
        img = img[lx:rx, by:upy]
        cropped_data.append(img)
    return cropped_data

def croping_image(path, path_save):
    dirs = os.listdir(path)
    dirsave = os.listdir(path_save)
    clearing_files(path_save)
    imgCount = int(len(dirs))
    count = 1
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            x = 5
            """
            new_image = im.crop((150+x, 205+x, 585, 635))
            new_image.save(path_save+"a_"+str(count)+".jpg")
            new_image = im.crop((635+x, 200+x, 1075, 630))
            new_image.save(path_save+"i_"+str(count)+".jpg")
            new_image = im.crop((1120+x, 195+x, 1555, 625))
            new_image.save(path_save+"u_"+str(count)+".jpg")

            new_image = im.crop((150+x, 722+x, 590, 1155))
            new_image.save(path_save+"e_"+str(count)+".jpg")
            new_image = im.crop((645+x, 720+x, 1080, 1140))
            new_image.save(path_save+"o_"+str(count)+".jpg")
            new_image = im.crop((1125+x, 711+x, 1560, 1135))
            new_image.save(path_save+"eu_"+str(count)+".jpg")

            new_image = im.crop((165+x, 1235+x, 595, 1660))
            new_image.save(path_save+"ae_"+str(count)+".jpg")
            new_image = im.crop((655+x, 1230+x, 1085, 1650))
            new_image.save(path_save+"8_"+str(count)+".jpg")
            new_image = im.crop((1135+x, 1220+x, 1565, 1645))
            new_image.save(path_save+"9_"+str(count)+".jpg")

            new_image = im.crop((175+x, 1735+x, 600, 2165))
            new_image.save(path_save+"10_"+str(count)+".jpg")
            new_image = im.crop((665+x, 1730+x, 1095, 2155))
            new_image.save(path_save+"11_"+str(count)+".jpg")
            new_image = im.crop((1145+x, 1725+x, 1570, 2150))
            new_image.save(path_save+"12_"+str(count)+".jpg")
            """
            """
            new_image = im.crop((150+x, 205+x, 585, 635))
            new_image.save(path_save+"ka_"+str(count)+".jpg")
            new_image = im.crop((635+x, 200+x, 1075, 630))
            new_image.save(path_save+"ca_"+str(count)+".jpg")
            new_image = im.crop((1120+x, 195+x, 1555, 625))
            new_image.save(path_save+"ta_"+str(count)+".jpg")

            new_image = im.crop((150+x, 722+x, 590, 1155))
            new_image.save(path_save+"pa_"+str(count)+".jpg")
            new_image = im.crop((645+x, 720+x, 1080, 1140))
            new_image.save(path_save+"ya_"+str(count)+".jpg")
            new_image = im.crop((1125+x, 711+x, 1560, 1135))
            new_image.save(path_save+"wa_"+str(count)+".jpg")

            new_image = im.crop((165+x, 1235+x, 595, 1660))
            new_image.save(path_save+"ga_"+str(count)+".jpg")
            new_image = im.crop((655+x, 1230+x, 1085, 1650))
            new_image.save(path_save+"ja_"+str(count)+".jpg")
            new_image = im.crop((1135+x, 1220+x, 1565, 1645))
            new_image.save(path_save+"da_"+str(count)+".jpg")

            new_image = im.crop((175+x, 1735+x, 600, 2165))
            new_image.save(path_save+"ba_"+str(count)+".jpg")
            new_image = im.crop((665+x, 1730+x, 1095, 2155))
            new_image.save(path_save+"ra_"+str(count)+".jpg")
            new_image = im.crop((1145+x, 1725+x, 1570, 2150))
            new_image.save(path_save+"sa_"+str(count)+".jpg")
            """
            new_image = im.crop((150+x, 205+x, 585, 635))
            new_image.save(path_save+"nga_"+str(count)+".jpg")
            new_image = im.crop((635+x, 200+x, 1075, 630))
            new_image.save(path_save+"nya_"+str(count)+".jpg")
            new_image = im.crop((1120+x, 195+x, 1555, 625))
            new_image.save(path_save+"na_"+str(count)+".jpg")

            new_image = im.crop((150+x, 722+x, 590, 1155))
            new_image.save(path_save+"ma_"+str(count)+".jpg")
            new_image = im.crop((645+x, 720+x, 1080, 1140))
            new_image.save(path_save+"la_"+str(count)+".jpg")
            new_image = im.crop((1125+x, 711+x, 1560, 1135))
            new_image.save(path_save+"ha_"+str(count)+".jpg")

            new_image = im.crop((165+x, 1235+x, 595, 1660))
            new_image.save(path_save+"qa_"+str(count)+".jpg")
            new_image = im.crop((655+x, 1230+x, 1085, 1650))
            new_image.save(path_save+"va_"+str(count)+".jpg")
            new_image = im.crop((1135+x, 1220+x, 1565, 1645))
            new_image.save(path_save+"xa_"+str(count)+".jpg")

            new_image = im.crop((175+x, 1735+x, 600, 2165))
            new_image.save(path_save+"za_"+str(count)+".jpg")
            new_image = im.crop((665+x, 1730+x, 1095, 2155))
            new_image.save(path_save+"fa_"+str(count)+".jpg")
            new_image = im.crop((1145+x, 1725+x, 1570, 2150))
            new_image.save(path_save+"12_"+str(count)+".jpg")

            progress(count, imgCount, "Croping Image")
            count+=1

def denoise(im, U_init, tolerance=0.1, tau=0.125, tv_weight=100):
    m, n = im.shape

    U = U_init
    Px = im
    Py = im
    error = 1

    while(error > tolerance):
        Uold = U

        GradUx = roll(U, -1, axis=1) - U
        GradUy = roll(U, -1, axis=0) - U

        PxNew = Px + (tau/tv_weight)*GradUx
        PyNew = Py + (tau/tv_weight)*GradUy
        NormNew = maximum(1, sqrt(PxNew**2+PyNew**2))

        PxNew = PxNew/NormNew
        PyNew = PyNew/NormNew

        RxPx = roll(Px, 1, axis=1)
        RyPy = roll(Py, 1, axis=0)

        DivP = (Px-RxPx) + (Py-RyPy)
        U = im + tv_weight*DivP

        error = linalg.norm(U-Uold)

    return U, im-U
