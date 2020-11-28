import fpho_setup
import sys
from statistics import mean
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

pho_setup_DF = fpho_setup.import_fpho_data(animal_ID='vole1',
                                           exp_date='2020-09-01',
                                           exp_desc="testing",
                                           input_filename='SampleData/1fiberSignal.csv',
                                           output_filename='test.csv')

# Norm = fpho_setup.plot_1fiber_norm_iso(fpho_dataframe=pho_setup_DF)

Fit = fpho_setup.plot_1fiber_norm_fitted(fpho_dataframe=pho_setup_DF)

