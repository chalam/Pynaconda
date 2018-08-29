#https://speakerdeck.com/pycon2017/michele-pratusevich-instagram-filters-in-15-lines-of-python

import skimage
from skimage import io
original_image = skimage.io.imread('swiss_alps.jpg')
