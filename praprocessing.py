import os, sys
from PIL import Image
from utils import progress, clearing_files

def image_resized(path, path_save=None, size=None, test=None):
    dirs = os.listdir(path)
    clearing_files(path_save)

    imgCount = int(len(dirs))
    count = 1
    if test is None:
        for item in dirs:
            if os.path.isfile(path+item):
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                # print (f)
                imResize = im.resize((size,size), Image.ANTIALIAS)
                progress(count, imgCount, "Resizing Image")
                imResize.save(path_save + item, 'JPEG', quality=100)
                count+=1
    else:
        # for item in dirs:
            # if os.path.isfile(path+item):
        im = Image.open(path)
        # f, e = os.path.splitext(path+item)
        imResize = im.resize((size,size), Image.ANTIALIAS)
        # print (f)
        # progress(count, imgCount)
        # imResize.save(path_save + item, 'JPEG', quality=100)
        # count+=1
        return imResize
