import fpho_setup
import sys
from statistics import mean
import pandas as pd

pho_setup_DF = fpho_setup.import_fpho_data('SampleData/1fiberSignal.csv','test.csv')

# metadata_file = fpho_setup.make_summary_file(animal_num='1', exp_desc = 'Prairie dogs hanging out',exp_yyyy_mm_dd = "2000-12-01", summarycsv_name="summary.csv")
# print(metadata_file)

# print(pd.DataFrame.head(pho_setup_DF))

fpho_setup.raw_signal_trace(fpho_dataframe=pho_setup_DF,output_filename='test.png',data_row_index=0)
