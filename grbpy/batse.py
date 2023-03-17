import sys
import pandas as pd
import numpy as np



class BATSEBurst:

    def __init__(self, file_path, time_signature):
        accepted_time_signatures = ['64ms', 'tte', 'cont']
        if time_signature in accepted_time_signatures:
            self.time_signature = time_signature
        else:
            sys.exit(f'file_type must be one of: {accepted_time_signatures}')
        self.file_path = file_path
        self.meta_data = None
        self.raw_data = None
        self.chan_data = None

    def parse_file(self):
        f = open(self.file_path, 'r')
        if self.time_signature == '64ms':

            temp_meta_names = f.readline().split()[:4]
            temp_meta_data = f.readline().split()[:4]
            meta_dict = {}
            for i in range(len(temp_meta_names)):
                meta_dict[temp_meta_names[i]] = int(temp_meta_data[i])
            self.meta_data = meta_dict

            self.raw_data = f.read()
            header_names = ['chan1', 'chan2', 'chan3', 'chan4']
            self.chan_data = pd.read_csv(self.file_path, header=1, delimiter=r"\s+", names=header_names)
            self.chan_data['sum_chan'] = self.chan_data[list(self.chan_data.columns)].sum(axis=1)
            self.chan_data['trig_time'] = (np.arange(meta_dict['npts']) - meta_dict['nlasc']) * 0.064

    def summary(self, raw=False):
        if self.time_signature == '64ms':
            print(f'Meta Data: \n{self.meta_data}')
            print(f'Data: \n{self.chan_data}')
            if raw:
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
        self.dur_data = pd.read_csv(self.file_path, header=None, delimiter=r"\s+")
        self.dur_data.columns = self.header_names

    def summary(self, raw=False):
        print(f'See BATSE.md for Summary')
        print(self.dur_data)
        if raw:
            print(f'Raw data: \n{self.raw_data}')
