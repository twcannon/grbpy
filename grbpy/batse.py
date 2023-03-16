import os
import sys
import numpy as np


class BATSEBurst:

    def __init__(self, file_path, time_signature):
        accepted_time_signatures = ['64ms', 'tte', 'cont']
        if time_signature in accepted_time_signatures:
            self.time_signature = time_signature
        else:
            sys.exit(f'file_type must be one of: {accepted_time_signatures}')
        self.file_path = file_path
        self.header_names = None
        self.header_data = None
        self.raw_data = None
        self.ind_chan_data = None
        self.sum_chan_data = None

    def parse_file(self):
        f = open(self.file_path, 'r')
        if self.time_signature == '64ms':
            self.header_names = f.readline()
            self.header_data = f.readline()
            self.raw_data = f.read()
            self.ind_chan_data = np.genfromtxt(self.file_path, delimiter='  ', skip_header=2)
            self.sum_chan_data = self.ind_chan_data.sum(axis=1)

    def summary(self, raw=False):
        if self.time_signature == '64ms':
            print(f'Header: \n{self.header_names}{self.header_data}')
            if raw:
                print(f'Raw Header: \n{self.header_names}{self.header_data}')
                print(f'Raw data: \n{self.raw_data}')


class BATSEDurations:

    def __init__(self, file_path):
        self.file_path = file_path
        self.header_names = None
        self.raw_data = None
        self.dur_data = None

    def parse_file(self):
        f = open(self.file_path, 'r')
        self.header_names = ['trig_num', 't50', 't50e', 't50_start', 't90', 't90e', 't90_start']
        self.raw_data = f.read()
        self.dur_data = np.genfromtxt(self.file_path)

    def summary(self, raw=False):
        print(f'See BATSE.md for Summary')
        if raw:
            print(f'Raw data: \n{self.raw_data}')
