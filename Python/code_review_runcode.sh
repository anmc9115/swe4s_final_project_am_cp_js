# 1. For Rezgar Shakeri -----------------------------------------------------------------------------------------------
# Please review: import_fpho_data() function in fpho_setup.py
# The function opens a data file, parses its information, and outputs a dataframe
# Here is a bash command which runs the function:
python fpho_driver.py --input_filename SynchronyData/FiberPhoSig2020-10-12T15_30_41.csv --output_filename T15_30_41.csv
# For user commands enter: 
# Please enter <1> if one fiber data or <2> if two fiber data: 1
# Which column contains f1Red information? Please enter <3> or <4> indicating column index: 3
# You indicated that column 3 contains f1Red and column 4 contains f1Green. Is this correct (yes or no)? yes
# outputs a csv called T15_30_41.csv

# 2. For Leila Ghaffari -----------------------------------------------------------------------------------------------
# Please review: raw_signal_trace() and plot_1fiber_norm_iso() in fpho_setup.py
# Here is a bash command which runs the raw signal plot:
python fpho_driver.py --input_filename SynchronyData/FiberPhoSig2020-10-12T15_30_41.csv --output_filename T15_30_41.csv --plot_raw_signal 1
# For user commands enter:
# One fiber or two fiber input data?
# Please enter <1> if one fiber data or <2> if two fiber data: 1
# Which column contains f1Red information? Please enter <3> or <4> indicating column index: 3
# You indicated that column 3 contains f1Red and column 4 contains f1Green. Is this correct (yes or no)? y
# Moving forward...
# Output CSV written to T15_30_41.csv
# ----------
# What channel(s) would you like to plot?
# Options are f1Red, f2Red, f1Green, f2Green.
# If plotting multiple channels, please separate with a space or comma.
# ----------
# Selection: f1Green
# outputs png called: T15_30_41_f1GreenGreen_rawsig.png

# Here is are bash commands which run the fitted isosbestic plot (the first must be run for the second to work):
python fpho_driver.py --input_filename SynchronyData/FiberPhoSig2020-10-12T15_30_41.csv --output_filename T15_30_41.csv
# For user commands enter: 
# Please enter <1> if one fiber data or <2> if two fiber data: 1
# Which column contains f1Red information? Please enter <3> or <4> indicating column index: 3
# You indicated that column 3 contains f1Red and column 4 contains f1Green. Is this correct (yes or no)? yes
python check.py

# 3. For Clair Huffine -----------------------------------------------------------------------------------------------
# Please review: fpho_driver.py, test_fpho_setup.py
# Look above for example bash commands that use the driver
