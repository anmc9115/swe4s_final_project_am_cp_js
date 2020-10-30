"""Library of functions for fpho_driver

    * import_fpho_data - saves data from csv in lists
    * make_summary_file - outputs txt file of summary info
    * plot_1fiber_norm_fitted - Plots 1 fiber normalized fitted exponenent
    * plot_2fiber_norm_fitted - Plots 2 fiber normalized fitted exponenent
    * plot_1fiber_norm_iso - Plots 1 fiber normalized isosbestic fit
    * plot_2fiber_norm_iso - PLots 2 fiber normalized isosbestic fit

"""
import sys
from statistics import mean
import pandas as pd

driver_version = 'v2.0'

# Variable for what fiber1 is (animal_num, side of brain, etc)
# Variable for what fiber2 is (animal_num, side of brain, etc)
def import_fpho_data(file_name): # USER INPUTS
    """Takes a file name, returns lists of parsed data

        Parameters
        ----------
        file_name: string
                The path to the CSV file

        Returns:
        --------
        twofiber_fdata: list
                containing f1GreenIso, f1GreenRed, f1GreenGreen,
                           f2GreenIso, f2GreenRed, f2GreenGreen,
                           f1RedIso, f1RedRed, f1RedGreen,
                           f2RedIso, f2RedRed, f2RedGreen,
                           fTimeIso, fTimeRed, fTimeGreen
                name depcits fiber number, channel, color
        onefiber_fdata: list
                containing f1GreenIso, f1GreenRed, f1GreenGreen,
                           f1RedIso, f1RedRed, f1RedGreen,
                           fTimeIso, fTimeRed, fTimeGreen
                name depcits fiber number, channel, color
        """
    # Open file, catch errors
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("Could not find file: " + file_name)
        sys.exit(1)
    except PermissionError:
        print("Could not access file: " + file_name)
        sys.exit(2)

    fTime = []
    f1Red = []
    f1Green = []
    f2Red = []
    f2Green = []
    twoFiber = False

    # TO DO: assignment is not the same every time!
    # User input for the order in fData
    for line in file:
        columns = line.rstrip().split(',')
        fTime.append(float(columns[0]))
        f1Red.append(float(columns[2]))
        f1Green.append(float(columns[3]))
        if columns[4] and columns[5] is not None:
            f2Red.append(float(columns[4]))
            f2Green.append(float(columns[5]))
            twoFiber = True

    file.close()
    
    # Trim first ~5sec from data
    f1Green = f1Green[250:]
    f1Red = f1Red[250:]
    f2Green = f2Green[250:]
    f2Red = f2Red[250:]
    fTime = fTime[250:]

    # De-interleave
    offset1 = f1Green[0::3]  # takes every 3rd element
    offset2 = f1Green[1::3]
    offset3 = f1Green[2::3]
    meanoffsets = [mean(offset1), mean(offset2), mean(offset3)]

    # Green has highest signal (GcAMP)
    # Order: green(470), red(560), iso(415)
    greenIdX = meanoffsets.index(max(meanoffsets))
    redIdX = greenIdX+1
    isoIdX = greenIdX+2

    # Assigning correct rows to colors
    # First fiber, green
    f1GreenIso = f1Green[greenIdX::3]
    f1GreenRed = f1Green[redIdX::3]
    f1GreenGreen = f1Green[isoIdX::3]

    # First fiber, red
    f1RedIso = f1Red[greenIdX::3]
    f1RedRed = f1Red[redIdX::3]
    f1RedGreen = f1Red[isoIdX::3]

    # Sorting time by color
    fTimeIso = fTime[greenIdX::3]
    fTimeRed = fTime[redIdX::3]
    fTimeGreen = fTime[isoIdX::3]

    if twoFiber:
        # Second fiber, green
        f2GreenIso = f2Green[greenIdX::3]
        f2GreenRed = f2Green[redIdX::3]
        f2GreenGreen = f2Green[isoIdX::3]

        # Second fiber, red
        f2RedIso = f2Red[greenIdX::3]
        f2RedRed = f2Red[redIdX::3]
        f2RedGreen = f2Red[isoIdX::3]

        # TO DO: Make dataframe holding each of these (pandas time)
        # File name as big header
        twofiber_fdata = [f1GreenIso, f1GreenRed, f1GreenGreen,
                          f2GreenIso, f2GreenRed, f2GreenGreen,
                          f1RedIso, f1RedRed, f1RedGreen,
                          f2RedIso, f2RedRed, f2RedGreen,
                          fTimeIso, fTimeRed, fTimeGreen]

        return twofiber_fdata

    onefiber_fdata = [f1GreenIso, f1GreenRed, f1GreenGreen,
                      f1RedIso, f1RedRed, f1RedGreen,
                      fTimeIso, fTimeRed, fTimeGreen]
    return onefiber_fdata


def make_summary_file(data_frame, output_filename):
    """Creates a file that holds important information

        Parameters
        ----------
        animal_num: integer
                Number of the animal
        date: string
                Date of the experiment
        exp: string
                Brief description of experiment

        Returns:
        --------
        summary_info: text file
            file containing: version, animal_num, date, exp,
        """
    # their own row in the dataframe


def raw_signal_trace() #argument: fdataframe
    # plot each signal
    # 1. green in f1Green
    # 2. red in f1Red
    # 3. green in f2Green
    # 4. red in f2Red


# outputs fitted exp graph, returns normalized data (append to dataframe)
# ask user which channels to normalize and how (iso vs fitted exp)
# could add all for now and change later
def plot_fitted_exp(fData):
    """Plots fiberpho signal normalized to fitted exponent

        Parameters
        ----------
        fData: dataframe        

        Returns:
        --------
        norm_fitted_exp: plot
                A plot of fitted signal
        """
    # 4 graphs, 1 for each channel
    # Each graph:
        # 1. smoothed signal smooth(raw_trace)
        # 2. fitted exp
        # this is a santiy check!
    # Return normalized 

def plot_norm_iso():
    """Plots fiberpho signal normalized to isosbestic

        Parameters
        ----------
        fTime: float list
                A list containing time of the day in msec
        f1Red: float list
                A list containing red fluorescent values from fiber
        f1Green: float list
                A list containing green fluorescent values from fiber

        Returns:
        --------
        norm_iso: plot
                A plot of normalized signal
        """
    # 4 graphs, 1 for each channel
    # Each graph:
        # 1. smoothed signal smooth(raw_trace)
        # 2. fitted iso


# TEST DELETE
fData = import_fpho_data('Data/2FiberSignal.csv')
plot_2fiber_norm_fitted(fData)