# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:21:42 2019

@author: Bryan
"""

import load_file as lf

fname = '2019-04-27.csv'
fname_zip = '2019-04-27.zip'
data_dir = r'D:\Root.Ad.Auction\Data\1'

df = lf.load_data(fname=fname, data_dir=data_dir, Verbose=True)

    
    