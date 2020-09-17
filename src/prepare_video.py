import os
import cv2
import sys
import numpy as np
import logging

sys.path.remove( '/home/sebastian/Documents/calcium_imaging_analysis')
sys.path.remove( '/home/sebastian/CaImAn')

import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import src.configuration
from src.cropping import main_cropping as crop_function

file_name = 'm57697-05232018161615-0000.avi'
mouse = 57697

input_file_path = os.environ['DATA_DIR_LOCAL'] + 'behaviour/data/videos/m' + f'{mouse}' '/' + file_name
if not os.path.isfile(input_file_path):
    print('ERROR: File not found')

cap = cv2.VideoCapture(input_file_path)

try:
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
except:
    logging.info('Roll back to opencv 2')
    length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

if length == 0 or width == 0 or height == 0:  # CV failed to load
    cv_failed = True

dims = [length, height, width]
limits = False
ret, frame = cap.read()
while limits == False:

    figure, axes = plt.subplots(1)
    axes.imshow(frame)
    figure.show()

    y_ = int(input("Limit X1 : "))
    _y = int(input("Limit X2 : "))
    x_ = int(input("Limit Y1 : "))
    _x = int(input("Limit Y2 : "))

    rect = Rectangle((y_, x_), _y - y_, _x - x_, fill=False, color='r', linestyle='-', linewidth=2)
    axes.add_patch(rect)
    figure.show()

    limits_ok = str(input("Limits ok?: yes/no"))
    if limits_ok == 'yes':
        limits = True

output_file_path = os.environ['DATA_DIR_LOCAL'] + 'behaviour/data/cropped/m' + f'{mouse}' '/' + file_name
#out = cv2.VideoWriter(output_file_path, -1, 20.0, (_x-x_,_y-y_))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
output_video = cv2.VideoWriter(output_file_path, fourcc, 30, (_y-y_,_x-x_))

time = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    crop_img = frame[x_:_x, y_:_y, :]
    output_video.write(crop_img)

    #print(time)
    time = time + 1

output_video.release()
cap.release()

