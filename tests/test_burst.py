from grbpy.experiments.batse import BATSEBurst, BATSEDuration

burst_file_path = 'tests/sample_data/cat64ms.00143'
test_burst = BATSEBurst(file_path)
test_burst.parse_file()
test_burst.summary(raw=True)


duration_file_path = 'tests/sample_data/duration_table.txt'
dur_table = BATSEDuration(file_path)
dur_table.parse_file()
dur_table.summary(raw=True)
