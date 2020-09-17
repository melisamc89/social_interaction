import os
import cv2
import numpy as np
import logging

def main_cropping(mouse = None, file_name = None, cropping_limits = None):


    input_file_path = os.environ['DATA_DIR_LOCAL'] + 'behaviour/data/videos/m' + f'{mouse}' '/' + file_name
    output_file_path = os.environ['DATA_DIR_LOCAL'] + 'behaviour/data/cropped/m' + f'{mouse}' '/' + file_name

    if not os.path.isfile(input_file_path):
        print('ERROR: File not found')

    cap =  cv2.VideoCapture(input_file_path)

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


    return output_file_path