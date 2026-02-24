# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 15:11:54 2026

@author: LabUser
"""

from matplotlib import pyplot as plt
import numpy as np
import os
import shutil

doodle_icons = r"C:\Users\LabUser\OneDrive - Universiteit Utrecht\_LerenKijken\Experiments Folder\Exp-1-Bagage-search-v1\doodle icons"

png_iconspath = 'C:\\Users\\LabUser\\OneDrive - Universiteit Utrecht\\_LerenKijken\\Experiments Folder\\Exp-1-Bagage-search-v1\\doodle icons\\PNG icons\\' 
svg_iconspath = 'C:\\Users\\LabUser\\OneDrive - Universiteit Utrecht\\_LerenKijken\\Experiments Folder\\Exp-1-Bagage-search-v1\\doodle icons\\SVG icons\\' 

os.chdir(doodle_icons)

def list_files_walk(start_path='.'):
    all_files = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            all_files.append(os.path.join(root, file))
            
    return all_files

all_icons_png = list_files_walk(doodle_icons+r'\PNG')

for src in all_icons_png:
    p = src.split('\\')
    # dst = png_iconspath + p[-1]
    # shutil.copy(src, dst) 
    
    # for svg
    dst_svg = svg_iconspath + p[-1][:-3] + 'svg' 
    
    p[8] = 'SVG'
    p[-1] = p[-1][:-3] + 'svg' 
    src_svg = '\\'.join(p)
    shutil.copy(src_svg, dst_svg)

# os.chdir(r"C:\Users\LabUser\OneDrive - Universiteit Utrecht\_LerenKijken\Experiments Folder\UMU exp\image gen files")


# for i in range(50):
#     y = np.random.random((250,250))    
#    # plt.imsave(f'imgs/rand_noise_{str(i)}.png', y, cmap='gray')

    
    
    
for i in os.listdir(svg_iconspath):
    print('"doodle icons/SVG icons/'+i+'",')