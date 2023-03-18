from grbpy.batse import BATSEBurst, BATSEDurations

burst_file_path = 'sample_data/cat64ms.00143'
test_burst = BATSEBurst(file_path=burst_file_path, time_signature='64ms')
if test_burst.parse_file():
    test_burst.summary(raw=False)


duration_file_path = 'sample_data/duration_table.txt'
dur_table = BATSEDurations(file_path=duration_file_path)
if dur_table.parse_file():
    dur_table.summary(raw=False)
