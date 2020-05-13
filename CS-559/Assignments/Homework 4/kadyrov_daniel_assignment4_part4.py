# Daniel Kadyrov
# CS 559 - Machine Learning
# Homewowrk 4 
# Problem 4

'''
Modified from the script of the same name from : 
https://github.com/gskielian/JPG-PNG-to-MNIST-NN-Format
'''
import os
from PIL import Image
from array import *
from random import shuffle

# Load from and save to
Names = [['D:\kadyrov\Documents\Education\CS-559\Assignments\Homework 4\data\Handwriting\Processed','test']] #, ['./testing-images','t10k']]


for name in Names:
	
	data_image = array('B')
	data_label = array('B')

	FileList = []
	for dirname in os.listdir(name[0]): # [1:] Excludes .DS_Store from Mac OS
		path = os.path.join(name[0],dirname)
		for filename in os.listdir(path):
			if filename.endswith(".png"):
				FileList.append(os.path.join(name[0],dirname,filename))


	if name[1] == 'train':
		FileList = 3*FileList
		shuffle(FileList) # Usefull for further segmenting the validation set
		FileList = FileList[:60000]
	else:
		shuffle(FileList)

	for filename in FileList:

		label = int(filename.split('/')[2])

		Im = Image.open(filename)

		pixel = Im.load()

		width, height = Im.size

		for x in range(0,width):
			for y in range(0,height):
				data_image.append(pixel[y,x])

		data_label.append(label) # labels start (one unsigned byte each)

	hexval = "{0:#0{1}x}".format(len(FileList),6) # number of files in HEX

	# header for label array

	header = array('B')
	header.extend([0,0,8,1,0,0])
	header.append(int('0x'+hexval[2:][:2],16))
	header.append(int('0x'+hexval[2:][2:],16))
	
	data_label = header + data_label

	# additional header for images array

	if max([width,height]) <= 256:
		header.extend([0,0,0,width,0,0,0,height])
	else:
		raise ValueError('Image exceeds maximum size: 256x256 pixels');

	header[3] = 3 # Changing MSB for image data (0x00000803)
	
	data_image = header + data_image

	output_file = open(name[1]+'-images-idx3-ubyte', 'wb')
	data_image.tofile(output_file)
	output_file.close()

	output_file = open(name[1]+'-labels-idx1-ubyte', 'wb')
	data_label.tofile(output_file)
	output_file.close()

# gzip resulting files

for name in Names:
	os.system('gzip '+name[1]+'-images-idx3-ubyte')
	os.system('gzip '+name[1]+'-labels-idx1-ubyte')


# # %%
# from PIL import Image
# import numpy as np 
# import os
# import cv2 
# # %%
# im = Image.open('data\Handwriting\IMG_20200508_112313.jpg').convert("L")

# width, height = im.size

# for i in range(10):
#     for j in range(5):
#         y = np.append(y, [i+1])
#         img = im.crop((i*width/10, (j)*height/5, (i+1)*width/10, (j+1)*height/5))
#         img.save("data\Handwriting\{}_{}.png".format(i, j), "PNG")
#         img = np.resize(img, (28, 28, 1))
#         # x = np.append(x, np.array(img))
# # # # %%
# # # import cv2 
# # # import os 
# # # import pandas as pd

# # # x = np.array([])
# # # y = np.array([])
# # for file in os.listdir("data\Handwriting\Processed"):
# #     y = np.append(y, file.split("_")[0])
# # #     # break
# #     gray = cv2.imread(os.path.join("data\Handwriting\Processed", file), 0)
# #     gray = cv2.resize(gray, (28, 28)).flatten() / 255.0
# #     x = np.append(x, [gray])
# #     # y = np.append()

# # #     # if file.endswith(".txt"):
# # #         # print(os.path.join("/mydir", file))
# # %%
# x = np.array([])
# y = np.array([])
# def load_images_to_data(image_label, image_directory, features_data, label_data):
#     for file in os.listdir("data\Handwriting\Processed"):
#         img = Image.open(os.path.join("data\Handwriting\Processed", file)).convert("L")
#         img = np.resize(img, (28,28,1))
#         im2arr = np.array(img)
#         im2arr = im2arr.reshape(1,28,28,1)
#         features_data = np.append(features_data, im2arr, axis=0)
#         label_data = np.append(label_data, [image_label], axis=0)
#     return features_data, label_data


# x, y= load_images_to_data('1', 'data\\Handwriting\\Processed\\1_0', x, y)
# # # %%
# # x = []
# # y = []
# # for i in range(10):
# #     for j in range(5):
# #         y.append(i+1) #= np.append(y, [i+1])
# #         img = im.crop((i*width/10, (j)*height/5, (i+1)*width/10, (j+1)*height/5))
# #         img = np.resize(img, (28, 28, 1))
# #         # x = np.append(x, [np.array(img).reshape(1,28,28,1)], axis=0)
# #         x.append(np.array(img).reshape(1,28,28,1))
# # # y = np.where(y==10, 0, y)

# # # %%
# # from sklearn.model_selection import train_test_split

# # X_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=7)


# # # # %%


# # # %%


# # %%
