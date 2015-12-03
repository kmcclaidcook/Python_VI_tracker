from scipy import ndimage
import numpy as np
import os
from osgeo import gdal
#from collections import named tuple
#import sys

os.chdir('R:/RSofHighLatitudes/kb308/Data/Remote_Sensing/MODIS/MCD43A4_NBAR/North_America/')
filList = os.listdir('.')
bands = [1,2]

