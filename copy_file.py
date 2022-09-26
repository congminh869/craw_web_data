import glob
import os
from shutil import copy
# copyfile(src, dst)

if __name__ == "__main__":
	path_folders = ['IMG_0706', 'IMG_0707', 'IMG_0708', 'IMG_0709']
	path_dst = './data_img'
	count = 0
	for path_foler in path_folders:
		for path_img in glob.glob(path_foler+"/*.jpg"):
			copy(path_img, path_dst)
			count+=1
			print(count, path_img)
