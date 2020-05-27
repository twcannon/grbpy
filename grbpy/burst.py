import os
import sys
import numpy as np

class Burst:

    def __init__(self,file_path):
        self.file_path = file_path
        # print(self.file_path)



    def parse_batse_file(self):
        f = open(self.file_path, 'r')
        self.experiment = 'BATSE'
        self.header_names = f.readline()
        self.header_data = f.readline()
        self.raw_data = f.read()
        self.burst_data = np.genfromtxt(self.file_path, delimiter='  ',skip_header=2)



    def summary(self,raw=False):
        if self.experiment == 'BATSE':
            print(('Header: \n{}{}').format(self.header_names,self.header_data))
        if raw:
            print(('Raw Header: \n{}{}').format(self.header_names,self.header_data))
            print(('Raw data: \n{}').format(self.raw_data))