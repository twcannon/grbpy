from grbpy.burst import Burst

file_path = 'tests/sample_data/cat64ms.00143'
test_burst = Burst(file_path)
test_burst.parse_batse_file()
# test_burst.summary(raw=True)
test_burst.summary()