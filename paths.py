#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:41:08 2023
Script to easily access the filepaths on SSD 
@author: siljegrue
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage
import batch_processes, annotation, hyspec_io
import h5py


"""General paths"""
data_path = "/Volumes/MASTER_SSD/Article/Data" 
json_gray = "/Volumes/MASTER_SSD/Article/Data/label_classes.json" 


"""South side"""
annotation_dir_south_greyscale = "/Volumes/MASTER_SSD/Article/Data/South/Annotation_greyscale"
annotation_dir_south_classcolor = "/Volumes/MASTER_SSD/Article/Data/South/Annotation_classcolor"

hyspec_dir_south = "/Volumes/MASTER_SSD/Article/Data/South/4_Rad_Georef_SGC"



"""North Side"""

annotation_dir_north_greyscale = "/Volumes/MASTER_SSD/Article/Data/North/Annotation_greyscale/OlbergAreaN1"
annotation_dir_north_classcolor = "/Volumes/MASTER_SSD/Article/Data/North/Annotation_classbolor/OlbergAreaN1"
hyspec_dir_north = "/Volumes/MASTER_SSD/Article/Data/North/4_Rad_Georef_SGC"


# Read annotation metadata file, show classes
#class_dict = annotation.read_hasty_metadata(json_gray)
