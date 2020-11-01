import fpho_setup_dataframes
import sys
from statistics import mean
import pandas as pd

pho_setup_DF = fpho_setup_dataframes.import_fpho_data('Data/1fiberSignal.csv','test.csv')

metadata_file = fpho_setup_dataframes.make_summary_file(animal_num='1', exp = 'Prairie dogs hanging out',date = "2000-12-01", summarycsv_name="summary.csv")
print(metadata_file)

# fpho_setup_dataframes.raw_signal_trace(pho_setup_DF)
