import argparse
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import scipy.ndimage as pyimg
import random
import os

import utils

def parse_args():
	desc = "Convert an image to be used for training" 
	parser = argparse.ArgumentParser(description=desc)

	parser.add_argument('--image', type=str,
		default=None,
		help='Directory path to the image. (default: %(default)s)')

	parser.add_argument('--image_mask', type=str,
		default=None,
		help='Directory path to the image mask. (default: %(default)s)')

	parser.add_argument('--max_height', type=int, 
		default=None,
		help='Maximum height of the output images. (default: %(default)s)')


	args = parser.parse_args()
	return args

def resize(image, max = None):
	w,h = image.size
	r = w/h
	if max is not None:
		dim = (int(r*max), max)
		image = image.resize(dim)

	# return the resized image
	return image

def main():
	global args
	args = parse_args()
	filename =  os.path.splitext(os.path.basename(args.image))[0]
	mask_filename =  os.path.splitext(os.path.basename(args.image_mask))[0]

	img = Image.open(args.image)

	if args.max_height is not None:
		img = resize(img,args.max_height)
		processed_mask = resize(utils.text_image_preprocessing(args.image_mask),args.max_height)
	else:
		processed_mask = utils.text_image_preprocessing(args.image_mask)

	processed_mask.save(os.path.join('../data/style',mask_filename+'_processed.png'))

	dst = Image.new('RGB', (img.width + img.width, img.height))
	dst.paste(img, (img.width, 0))
	dst.paste(processed_mask, (0, 0))
	dst.save(os.path.join('../data/style',filename+'.png'))


if __name__ == "__main__":
	main()