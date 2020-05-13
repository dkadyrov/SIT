import glob
import os
from PIL import Image

def create_db():
	train_batch = open("./train_batch_img",'wb')
	train_batch_y = open("./train_batch_label",'wb')
	for file in glob.glob("./training-images/*.jpg"):
       	imgx = Image.open(file)
       	img = np.asarray(img, dtype='float64') / 256.
       	pickle.dump(img,train_batch)
       	pickle.dump(folder_name,train_batch_y)
   	train_batch.close()
   	train_batch_y.close()

create_db()