#!/usr/bin/env python

import keras
import os, shutil

#directory of og dataset
og_dir = 'puppyKitty_og_dataset'

#directory of mod dataset
mod_dir = 'puppyKitty_small'
os.mkdir(mod_dir)

#sub directories
train_dir = os.path.join(mod_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(mod_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(mod_dir, 'test')
os.mkdir(test_dir)

##training cats directory
train_kitty = os.path.join(train_dir, 'cats')
os.mkdir(train_kitty)

##training dogs directory
train_puppy = os.path.join(train_dir, 'dogs')
os.mkdir(train_puppy)

##validate cats directory
validate_kitty = os.path.join(validation_dir, 'cats')
os.mkdir(validate_kitty)

##validate dogs directory
validate_puppy = os.path.join(validation_dir, 'dogs')
os.mkdir(validate_puppy)

##test cats directory
test_kitty = os.path.join(test_dir, 'cats')
os.mkdir(test_kitty)

##test dogs directory
test_puppy = os.path.join(test_dir, 'dogs')
os.mkdir(test_puppy)

#copy 1000 cat images from database to training directory
imgName = ['cat.{}.jpg'.format(i) for i in range(1,1000)]
for imgName in imgName:
	src = os.path.join(og_dir, imgName)
	dst = os.path.join(train_kitty, imgName)
	shutil.copyfile(src, dst)

#copy 500 cat images from database to validation directory
imgName = ['cat.{}.jpg'.format(i) for i in range(1001,1500)]
for imgName in imgName:
	src = os.path.join(og_dir, imgName)
	dst = os.path.join(validate_kitty, imgName)
	shutil.copyfile(src, dst)

#copy 500 cat images from database to test directory
imgName = ['cat.{}.jpg'.format(i) for i in range(1501,2000)]
for imgName in imgName:
	src = os.path.join(og_dir, imgName)
	dst = os.path.join(test_kitty, imgName)
	shutil.copyfile(src, dst)

#copy 1000 dog images from database to training directory
imgName = ['dog.{}.jpg'.format(i) for i in range(1,1000)]
for imgName in imgName:
	src = os.path.join(og_dir, imgName)
	dst = os.path.join(train_puppy, imgName)
	shutil.copyfile(src, dst)

#copy 500 dog images from database to validation directory
imgName = ['dog.{}.jpg'.format(i) for i in range(1001,1500)]
for imgName in imgName:
	src = os.path.join(og_dir, imgName)
	dst = os.path.join(validate_puppy, imgName)
	shutil.copyfile(src, dst)

#copy 500 dog images from database to test directory
imgName = ['dog.{}.jpg'.format(i) for i in range(1501,2000)]
for imgName in imgName:
	src = os.path.join(og_dir, imgName)
	dst = os.path.join(test_puppy, imgName)
	shutil.copyfile(src, dst)





