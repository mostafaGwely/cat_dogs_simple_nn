# set the matplotlib backend so figures can be saved in the background
# import matplotlib
# matplotlib.use("Agg")
 
# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os

ap = argparse.ArgumentParser()

ap.add_argument('-d','--dataset',required=True,help="path to input dataset of images")
# ap.add_argument('-m','--model',required=True,help="path to the output trained model")
# ap.add_argument('-l','--label-bin',required=True,help="path to output label binarize")
# ap.add_argument('-p','--plot',required=True,help='path to the output accuracy/loss plot')

args = vars(ap.parse_args())

imagePaths = paths.list_images(args["dataset"])

for imagePath in imagePaths:
	print(imagePath)


