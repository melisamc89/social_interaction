'''

Created on Thru 22 Oct 2020
Author: Melisa

This script contains the steps into opening and construction the analysis for the
fly camera from data of the social interaction task, using single animal tracking version
of deeplabcut (DLC).

This will plot a few examples of the tracking for some body parts (using non filtered
and filtered output from DLC), using a particular threshold
for the likelihood of the tracking.

'''

import os
import src.configuration
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
cmap = cm.jet

output_figure_path = os.environ['PROJECT_DIR_LOCAL'] + 'figures/'
input_path = os.environ['DATA_DIR_LOCAL'] + 'm57697/'

name = 'm57697-05232018125955-0000'

input_file_path = input_path + name + 'DLC_resnet50_social_interaction_m57697okt20shuffle1_50000.csv'
input_file_path_filtered = input_path + name + 'DLC_resnet50_social_interaction_m57697okt20shuffle1_50000_filtered.csv'

tracking_data = pd.read_csv(input_file_path)
tracking_data_filtered = pd.read_csv(input_file_path_filtered)
body_parts = ['nose_1', 'ear1_1', 'ear2_1' , 'head_1', 'middle_body_1','tail_start_1','tail_middle_1','tail_end_1',
              'nose_2', 'ear1_2', 'ear2_2' , 'head_2', 'middle_body_2','tail_start_2','tail_middle_2','tail_end_2']

body_part_structure = ['x', 'y', 'likelihood']

tracking_data_array = tracking_data.to_numpy()
tracking_data_array_filtered = tracking_data_filtered.to_numpy()

LIKELIHOOD = 0.75

x_nose_1 = np.round(tracking_data_array[2:,1].astype(np.float),2)
y_nose_1 = np.round(tracking_data_array[2:,2].astype(np.float),2)
likelihood_nose_1 = np.round(tracking_data_array[2:,3].astype(np.float),2)

x_ear1_1 = np.round(tracking_data_array[2:,4].astype(np.float),2)
y_ear1_1 = np.round(tracking_data_array[2:,5].astype(np.float),2)
likelihood_ear1_1 = np.round(tracking_data_array[2:,6].astype(np.float),2)

x_ear2_1 = np.round(tracking_data_array[2:,7].astype(np.float),2)
y_ear2_1 = np.round(tracking_data_array[2:,8].astype(np.float),2)
likelihood_ear2_1 = np.round(tracking_data_array[2:,9].astype(np.float),2)

x_head_1 = np.round(tracking_data_array[2:,10].astype(np.float),2)
y_head_1 = np.round(tracking_data_array[2:,11].astype(np.float),2)
likelihood_head_1 = np.round(tracking_data_array[2:,12].astype(np.float),2)

selection_nose_1 = np.where(likelihood_nose_1>LIKELIHOOD)
selection_ear1_1 = np.where(likelihood_ear1_1>LIKELIHOOD)
selection_ear2_1 = np.where(likelihood_ear2_1>LIKELIHOOD)
selection_head_1 = np.where(likelihood_head_1>LIKELIHOOD)

intersec1_1 = np.intersect1d(selection_nose_1,selection_ear1_1)
intersec2_1 = np.intersect1d(selection_ear2_1,selection_head_1)
selection_1= np.intersect1d(intersec1_1,intersec2_1)


x_nose_2 = np.round(tracking_data_array[2:,25].astype(np.float),2)
y_nose_2 = np.round(tracking_data_array[2:,26].astype(np.float),2)
likelihood_nose_2 = np.round(tracking_data_array[2:,27].astype(np.float),2)

x_ear1_2 = np.round(tracking_data_array[2:,28].astype(np.float),2)
y_ear1_2 = np.round(tracking_data_array[2:,29].astype(np.float),2)
likelihood_ear1_2 = np.round(tracking_data_array[2:,30].astype(np.float),2)

x_ear2_2 = np.round(tracking_data_array[2:,31].astype(np.float),2)
y_ear2_2 = np.round(tracking_data_array[2:,32].astype(np.float),2)
likelihood_ear2_2 = np.round(tracking_data_array[2:,33].astype(np.float),2)

x_head_2 = np.round(tracking_data_array[2:,34].astype(np.float),2)
y_head_2 = np.round(tracking_data_array[2:,35].astype(np.float),2)
likelihood_head_2 = np.round(tracking_data_array[2:,36].astype(np.float),2)

selection_nose_2 = np.where(likelihood_nose_2>LIKELIHOOD)
selection_ear1_2 = np.where(likelihood_ear1_2>LIKELIHOOD)
selection_ear2_2 = np.where(likelihood_ear2_2>LIKELIHOOD)
selection_head_2 = np.where(likelihood_head_2>LIKELIHOOD)

intersec1_2 = np.intersect1d(selection_nose_2,selection_ear1_2)
intersec2_2 = np.intersect1d(selection_ear2_2,selection_head_2)
selection_2 = np.intersect1d(intersec1_2,intersec2_2)

selection = np.intersect1d(selection_1,selection_2)

new_x_nose_1 = x_nose_1[selection]
new_y_nose_1 = y_nose_1[selection]

new_x_ear1_1 = x_ear1_1[selection]
new_y_ear1_1 = y_ear1_1[selection]

new_x_ear2_1 = x_ear2_1[selection]
new_y_ear2_1 = y_ear2_1[selection]

new_x_head_1 = x_head_1[selection]
new_y_head_1 = y_head_1[selection]

new_x_nose_2 = x_nose_2[selection]
new_y_nose_2 = y_nose_2[selection]

new_x_ear1_2 = x_ear1_2[selection]
new_y_ear1_2 = y_ear1_2[selection]

new_x_ear2_2 = x_ear2_2[selection]
new_y_ear2_2 = y_ear2_2[selection]

new_x_head_2 = x_head_2[selection]
new_y_head_2 = y_head_2[selection]


figure = plt.figure()
axes = figure.add_subplot(111, projection='3d')
#color = np.linspace(0, 20, new_x.shape[0])
#axes.scatter(new_x,new_y, c = color, cmap = cmap)
#axes.plot(new_x_nose_1,new_y_nose_1)
#axes.plot(new_x_ear1_1,new_y_ear1_1)
#axes.plot(new_x_ear2_1,new_y_ear2_1)

time = np.arange(0,new_y_head_1.shape[0]/30 - 1/30,1/30)
axes.plot(new_x_head_1,new_y_head_1,time)
axes.plot(new_x_head_2,new_y_head_2,time)


axes.legend(['Head_Mouse_1', 'Head_Mouse_2'])
axes.set_xlabel('X [pixels]')
axes.set_ylabel('Y [pixels]')
axes.set_xlim([0,600])
axes.set_ylim([0,600])
figure.suptitle('Tracking. Likelihood:' + f'{LIKELIHOOD}')

figure.show()
output_figure_file_path = output_figure_path + name + '_likelihood_' + f'{LIKELIHOOD}' + '_3D.png'
figure.savefig(output_figure_file_path)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# compare non-filtered and filtered plots
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


name = 'm57697-05232018125955-0000'

input_file_path = input_path + name + 'DLC_resnet50_social_interaction_m57697okt20shuffle1_50000.csv'
input_file_path_filtered = input_path + name + 'DLC_resnet50_social_interaction_m57697okt20shuffle1_50000_filtered.csv'

tracking_data = pd.read_csv(input_file_path)
tracking_data_filtered = pd.read_csv(input_file_path_filtered)
body_parts = ['nose_1', 'ear1_1', 'ear2_1' , 'head_1', 'middle_body_1','tail_start_1','tail_middle_1','tail_end_1',
              'nose_2', 'ear1_2', 'ear2_2' , 'head_2', 'middle_body_2','tail_start_2','tail_middle_2','tail_end_2']

body_part_structure = ['x', 'y', 'likelihood']

#tracking_data_array = tracking_data.to_numpy()
tracking_data_array_filtered = tracking_data_filtered.to_numpy()

LIKELIHOOD = 0.75
tracking_data_array = tracking_data_array_filtered
x_nose_1 = np.round(tracking_data_array[2:,1].astype(np.float),2)
y_nose_1 = np.round(tracking_data_array[2:,2].astype(np.float),2)
likelihood_nose_1 = np.round(tracking_data_array[2:,3].astype(np.float),2)

x_ear1_1 = np.round(tracking_data_array[2:,4].astype(np.float),2)
y_ear1_1 = np.round(tracking_data_array[2:,5].astype(np.float),2)
likelihood_ear1_1 = np.round(tracking_data_array[2:,6].astype(np.float),2)

x_ear2_1 = np.round(tracking_data_array[2:,7].astype(np.float),2)
y_ear2_1 = np.round(tracking_data_array[2:,8].astype(np.float),2)
likelihood_ear2_1 = np.round(tracking_data_array[2:,9].astype(np.float),2)

x_head_1 = np.round(tracking_data_array[2:,10].astype(np.float),2)
y_head_1 = np.round(tracking_data_array[2:,11].astype(np.float),2)
likelihood_head_1 = np.round(tracking_data_array[2:,12].astype(np.float),2)

selection_nose_1 = np.where(likelihood_nose_1>LIKELIHOOD)
selection_ear1_1 = np.where(likelihood_ear1_1>LIKELIHOOD)
selection_ear2_1 = np.where(likelihood_ear2_1>LIKELIHOOD)
selection_head_1 = np.where(likelihood_head_1>LIKELIHOOD)

intersec1_1 = np.intersect1d(selection_nose_1,selection_ear1_1)
intersec2_1 = np.intersect1d(selection_ear2_1,selection_head_1)
selection_1= np.intersect1d(intersec1_1,intersec2_1)


x_nose_2 = np.round(tracking_data_array[2:,25].astype(np.float),2)
y_nose_2 = np.round(tracking_data_array[2:,26].astype(np.float),2)
likelihood_nose_2 = np.round(tracking_data_array[2:,27].astype(np.float),2)

x_ear1_2 = np.round(tracking_data_array[2:,28].astype(np.float),2)
y_ear1_2 = np.round(tracking_data_array[2:,29].astype(np.float),2)
likelihood_ear1_2 = np.round(tracking_data_array[2:,30].astype(np.float),2)

x_ear2_2 = np.round(tracking_data_array[2:,31].astype(np.float),2)
y_ear2_2 = np.round(tracking_data_array[2:,32].astype(np.float),2)
likelihood_ear2_2 = np.round(tracking_data_array[2:,33].astype(np.float),2)

x_head_2 = np.round(tracking_data_array[2:,34].astype(np.float),2)
y_head_2 = np.round(tracking_data_array[2:,35].astype(np.float),2)
likelihood_head_2 = np.round(tracking_data_array[2:,36].astype(np.float),2)

selection_nose_2 = np.where(likelihood_nose_2>LIKELIHOOD)
selection_ear1_2 = np.where(likelihood_ear1_2>LIKELIHOOD)
selection_ear2_2 = np.where(likelihood_ear2_2>LIKELIHOOD)
selection_head_2 = np.where(likelihood_head_2>LIKELIHOOD)

intersec1_2 = np.intersect1d(selection_nose_2,selection_ear1_2)
intersec2_2 = np.intersect1d(selection_ear2_2,selection_head_2)
selection_2 = np.intersect1d(intersec1_2,intersec2_2)

selection = np.intersect1d(selection_1,selection_2)

new_x_nose_1 = x_nose_1[selection]
new_y_nose_1 = y_nose_1[selection]

new_x_ear1_1 = x_ear1_1[selection]
new_y_ear1_1 = y_ear1_1[selection]

new_x_ear2_1 = x_ear2_1[selection]
new_y_ear2_1 = y_ear2_1[selection]

new_x_head_1 = x_head_1[selection]
new_y_head_1 = y_head_1[selection]

new_x_nose_2 = x_nose_2[selection]
new_y_nose_2 = y_nose_2[selection]

new_x_ear1_2 = x_ear1_2[selection]
new_y_ear1_2 = y_ear1_2[selection]

new_x_ear2_2 = x_ear2_2[selection]
new_y_ear2_2 = y_ear2_2[selection]

new_x_head_2 = x_head_2[selection]
new_y_head_2 = y_head_2[selection]


figure = plt.figure()
axes = figure.add_subplot(111, projection='3d')
#color = np.linspace(0, 20, new_x.shape[0])
#axes.scatter(new_x,new_y, c = color, cmap = cmap)
#axes.plot(new_x_nose_1,new_y_nose_1)
#axes.plot(new_x_ear1_1,new_y_ear1_1)
#axes.plot(new_x_ear2_1,new_y_ear2_1)

time = np.arange(0,new_y_head_1.shape[0]/30 - 1/30,1/30)
axes.plot(new_x_head_1,new_y_head_1,time)
axes.plot(new_x_head_2,new_y_head_2,time)


axes.legend(['Head_Mouse_1', 'Head_Mouse_2'])
axes.set_xlabel('X [pixels]')
axes.set_ylabel('Y [pixels]')
axes.set_xlim([0,600])
axes.set_ylim([0,600])
figure.suptitle('Tracking. Likelihood:' + f'{LIKELIHOOD}')

figure.show()
output_figure_file_path = output_figure_path + name + '_likelihood_' + f'{LIKELIHOOD}' + '_3D_filtered.png'
figure.savefig(output_figure_file_path)