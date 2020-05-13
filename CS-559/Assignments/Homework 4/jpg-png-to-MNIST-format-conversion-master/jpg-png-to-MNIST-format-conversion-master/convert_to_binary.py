from skimage import io, img_as_float
import numpy as np
import os

dir_name = "test-images/"

for i in range(1, 10):
    str_i = str(i)
    for filename in os.listdir(dir_name + str_i):
        image = io.imread(dir_name + str_i + "/" + filename)
        image = img_as_float(image)
        files = os.path.splitext(filename)
        fullname = os.path.join(dir_name, str_i, files[0] + "." + "jpg")
        os.remove(os.path.join(dir_name, str_i, files[0] + "." + "png"))
        io.imsave(fullname, image)