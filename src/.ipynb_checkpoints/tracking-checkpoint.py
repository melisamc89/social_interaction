'''

Created on Fri 09 Oct 2020
Author: Melisa

Script to open pickle files from social interaction experiment.
'''


import os
import src.configuration
import pickle
import math

## mouse number
mouse = 57697

## social interaction behaviour directory
social_interaction_dir = os.environ['DATA_DIR_LOCAL'] +'multianimaltracking/' +'m' + f'{mouse}' + '/'

## load tracking information as pickle
tracking_file_path = social_interaction_dir + 'm57697-05212018190408-0000DLC_resnet50_social_interaction_m57697sep17shuffle1_50000_full.pickle'
tracking_file = open(tracking_file_path , 'rb')
tracking_info = pickle.load(tracking_file)#, encoding='bytes')

time_point = tracking_info['frame08505']
coordinates = time_point['coordinates']
likelihood = time_point['likelihood']
