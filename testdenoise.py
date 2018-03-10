from PIL import Image
from pylab import *
import utils

im = array(Image.open('wisma-nusantara.jpg').convert('L'))
U, T = utils.denoise(im, im)

figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()
