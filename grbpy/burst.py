import os
import sys
import numpy as np


class Burst:

    def __init__(self, file_path, experiment):
        accepted_experiments = ['BATSE64ms']
        if experiment in accepted_experiments:
            self.experiment = experiment
        else:
            sys.exit(f'file_type must be one of: {accepted_experiments}')
        self.file_path = file_path
        self.header_names = None
        self.header_data = None
        self.raw_data = None
        self.ind_chan_data = None
        self.sum_chan_data = None

    def parse_file(self):
        f = open(self.file_path, 'r')
        if self.experiment == 'BATSE64ms':
            self.header_names = f.readline()
            self.header_data = f.readline()
            self.raw_data = f.read()
            self.ind_chan_data = np.genfromtxt(self.file_path, delimiter='  ', skip_header=2)
            self.sum_chan_data = self.ind_chan_data.sum(axis=1)

    def summary(self, raw=False):
        if self.experiment == 'BATSE64ms':
            print(f'Header: \n{self.header_names}{self.header_data}')
            if raw:
                print(f'Raw Header: \n{self.header_names}{self.header_data}')
                print(f'Raw data: \n{self.raw_data}')
