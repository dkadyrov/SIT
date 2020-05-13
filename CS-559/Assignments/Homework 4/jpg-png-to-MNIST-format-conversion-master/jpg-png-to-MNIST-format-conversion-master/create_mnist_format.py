import os
import pickle
import numpy as np
import glob
from PIL import Image
from skimage import io, img_as_float

training_set_image = np.empty(shape=[0, 784])
training_set_labels = np.empty(shape=[0, 1])

test_set_image = np.empty(shape=[0, 784])
test_set_labels = np.empty(shape=[0, 1])

def create_set(setValue):   #setValue = 1 => training_set, setValue = 2 => test_set
    
    if(setValue == 1):
        targetFolder = "training-images"
    else:
        targetFolder = "test-images"

    numFolders = 10

    for index in range(1, numFolders):

        label = index

        for file in glob.glob("./" + targetFolder + "/" + str(index) + "/*.jpg"):
            image = io.imread(file)
            image = img_as_float(image)
            li = []
            for x in range(0, 28):
                for y in range(0, 28):
                    li.append(image[x][y])

            if(setValue == 1):
                global training_set_image
                global training_set_labels
                training_set_image = np.append(training_set_image, [li], axis=0)
                training_set_labels = np.append(training_set_labels, [[label, ]], axis=0)
            else:
                global test_set_image
                global test_set_labels
                test_set_image = np.append(test_set_image, [li], axis=0)
                test_set_labels = np.append(test_set_labels, [[label, ]], axis=0)                

        index = index + 1

def create_training_set():
    create_set(1)

def create_test_set():
    create_set(2)

def pickleData():

    set_list = [(training_set_image, training_set_labels), (test_set_image, test_set_labels)]

    PIK = "custom-data-pickle.dat"

    with open(PIK, "ab") as fileOpen:
        pickle.dump(set_list, fileOpen)

create_training_set()
create_test_set()

pickleData()



