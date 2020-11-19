"""Library of functions for fpho_driver

    * import_fpho_data - saves data from csv in lists
    * make_summary_file - outputs txt file of summary info
    * plot_1fiber_norm_fitted - Plots 1 fiber normalized fitted exponenent
    * plot_2fiber_norm_fitted - Plots 2 fiber normalized fitted exponenent
    * plot_1fiber_norm_iso - Plots 1 fiber normalized isosbestic fit
    * plot_2fiber_norm_iso - PLots 2 fiber normalized isosbestic fit

"""

# Claire to-do: Add warning message when columns are different lengths

import sys
from statistics import mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

driver_version = 'v2.0'


def import_fpho_data(input_filename, output_filename):
    """Takes a file name, returns a dataframe of parsed data

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

    # User questions to specify type of information in columns of input data

    # User input to indicate one fiber or two fiber data
    fiber_val = input("\nOne fiber or two fiber input data?\n"
                      + "Please enter <1> if one fiber data "
                      + "or <2> if two fiber data: ")

    try:
        fiber_val = int(fiber_val)
    except ValueError:
        print("Error: Invalid input."
              + "Please restart and use integer input to indicate "
              + "number of fibers represented in input data.\n")
        sys.exit(1)

    while fiber_val not in [1, 2]:
        print("Error: Integer entered for number of "
              + "fibers represented in dataset <"
              + str(fiber_val) + "> was invalid."
              + " Please enter <1> or <2> or press any letter to exit.")
        fiber_val = input()
        if type(fiber_val) != int:
            sys.exit()

    # User input to find out which column contains info for the f1Red channel
    f1Red_col = input("\nWhich column contains f1Red information? "
                      + "Please enter <3> or <4> indicating column index: ")
    try:
        f1Red_col = int(f1Red_col)
    except ValueError:
        print("Error: Column index not entered as integer. Restarting")

    while f1Red_col not in [3, 4]:
        print("\nError: Your input <" + str(f1Red_col) + "> was invalid. "
              + "Enter either <3> or <4> or press any letter to exit.\n")
        f1Red_col = input("Which column contains f1Red information?\n"
                          + "Enter <3> or <4>, or press any letter to exit: ")
        if type(f1Red_col) != int:
            sys.exit()

    if f1Red_col == 3:
        f1Green_col = 4
        while True:
            answer = input("\nYou indicated that column 3 contains f1Red"
                           + " and column 4 contains f1Green. "
                           + "Is this correct (yes or no)? ")
            if answer.lower().startswith("y"):
                print("Moving forward...\n")
                break
            elif answer.lower().startswith("n"):
                print("You replied no. Restarting data information entry")
                exit()
    else:
        f1Green_col = 3
        while True:
            answer = input("You indicated that column 3 contains f1Green"
                           + " and column 4 contains f1Red. "
                           + "Is this correct (yes or no)?\n")
            if answer.lower().startswith("y"):
                print("Moving forward...\n")
                break
            elif answer.lower().startswith("n"):
                print("You replied no. Please restart")
                sys.exit()

    # Begin 2 fiber if statement to get 2 fiber column info
    if fiber_val == 2:
        f2Red_col = int(input("Which column contains f2Red information?\n"
                              + "Please enter <5> or <6>:\n"))
        while f2Red_col not in [4, 5]:
            print("Your input", f2Red_col,
                  "is invalid.\nEnter either <5> or <6>, or 'x' to exit.\n")
            f2Red_col = input("Which column contains f2Red information?\n"
                              + "Please enter <5> or <6>:\n")
            if f2Red_col == 'x':
                exit()

        if f2Red_col == 5:
            f2Green_col = 6
            while True:
                answer = input("You indicated that column 5 contains f1Red "
                               + "and column 6 contains f1Green. "
                               + "Is this correct (yes or no)?\n")
                if answer.lower().startswith("y"):
                    print("Moving forward...\n")
                    break
                elif answer.lower().startswith("n"):
                    print("You replied no. Please restart")
                    exit()
        else:
            f2Green_col = 5
            while True:
                answer = input("You indicated that column 5 contains f1Green "
                               + "and column 6 contains f2Red. "
                               + "Is this correct (yes or no)?\n")
                if answer.lower().startswith("y"):
                    print("Moving forward...\n")
                    break
                elif answer.lower().startswith("n"):
                    print("You replied no. Please restart")
                    exit()

    fTime = []
    f1Red = []
    f1Green = []
    f2Red = []
    f2Green = []

    # Open file, catch errors
    try:
        file = open(input_filename, 'r')
    except FileNotFoundError:
        print("Could not find file: " + input_filename)
        sys.exit(1)
    except PermissionError:
        print("Could not access file: " + input_filename)
        sys.exit(2)

    for line in file:
        columns = line.rstrip().split(' ')
        fTime.append(float(columns[0]))
        f1Red.append(float(columns[f1Red_col-1]))
        f1Green.append(float(columns[f1Green_col-1]))
        if fiber_val == 2:
            f2Red.append(float(columns[f2Red_col-1]))
            f2Green.append(float(columns[f2Green_col-1]))

    file.close()

    # Trim first ~5sec from data
    f1Green = f1Green[250:]
    f1Red = f1Red[250:]
    f2Green = f2Green[250:]
    f2Red = f2Red[250:]
    fTime = fTime[250:]
    # print('starts',len(f1Green),len(f1Red),
    #       len(f2Green), len(f2Red), len(fTime))
    # Same Length

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
    # print('Idx',greenIdX,redIdX,isoIdX)

    # Assigning correct rows to colors
    # First fiber, green
    f1GreenIso = f1Green[greenIdX::3]
    f1GreenRed = f1Green[redIdX::3]
    f1GreenGreen = f1Green[isoIdX::3]
    # print('green',len(f1GreenIso),len(f1GreenRed),len(f1GreenGreen))

    # First fiber, red
    f1RedIso = f1Red[greenIdX::3]
    f1RedRed = f1Red[redIdX::3]
    f1RedGreen = f1Red[isoIdX::3]
    # print('red',len(f1RedIso),len(f1RedRed),len(f1RedGreen))

    # Sorting time by color
    fTimeIso = fTime[greenIdX::3]
    fTimeRed = fTime[redIdX::3]
    fTimeGreen = fTime[isoIdX::3]

    if fiber_val == 2:
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

        twofiber_fdata = pd.DataFrame({'f1GreenIso': pd.Series(f1GreenIso),
                                       'f1GreenRed': pd.Series(f1GreenRed),
                                       'f1GreenGreen': pd.Series(f1GreenGreen),
                                       'f2GreenIso': pd.Series(f2GreenIso),
                                       'f2GreenRed': pd.Series(f2GreenRed),
                                       'f2GreenGreen': pd.Series(f2GreenGreen),
                                       'f1RedIso': pd.Series(f1RedIso),
                                       'f1RedRed': pd.Series(f1RedRed),
                                       'f1RedGreen': pd.Series(f1RedGreen),
                                       'f2RedIso': pd.Series(f2RedIso),
                                       'f2RedRed': pd.Series(f2RedRed),
                                       'f2RedGreen': pd.Series(f2RedGreen),
                                       'fTimeIso': pd.Series(fTimeIso),
                                       'fTimeRed': pd.Series(fTimeRed),
                                       'fTimeGreen': pd.Series(fTimeGreen)})

        twofiber_fdata.to_csv(output_filename, index=False)
        print('Output CSV written to ' + output_filename)
        return twofiber_fdata

    else:
        onefiber_fdata = pd.DataFrame({'f1GreenIso': pd.Series(f1GreenIso),
                                       'f1GreenRed': pd.Series(f1GreenRed),
                                       'f1GreenGreen': pd.Series(f1GreenGreen),
                                       'f1RedIso': pd.Series(f1RedIso),
                                       'f1RedRed': pd.Series(f1RedRed),
                                       'f1RedGreen': pd.Series(f1RedGreen),
                                       'fTimeIso': pd.Series(fTimeIso),
                                       'fTimeRed': pd.Series(fTimeRed),
                                       'fTimeGreen': pd.Series(fTimeGreen)})

        onefiber_fdata.to_csv(output_filename, index=False, na_rep='')
        print('Output CSV written to ' + output_filename)
        return onefiber_fdata


def make_summary_file(animal_num, exp_yyyy_mm_dd, exp_desc, summarycsv_name):

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

    # metadata_df = pd.DataFrame({'animal_IDnum': animal_num,
    #                             'experiment_description': exp,
    #                             'experiment_date': date},
    #                             index=[0])

    try:
        datetime.datetime.strptime(exp_yyyy_mm_dd, '%Y-%m-%d')
    except ValueError:
        print('Date {'+exp_yyyy_mm_dd+'} not entered in correct format.'
              + ' Please re-enter in YYYY-MM-DD format.')
        # raise ValueError
        sys.exit(1)  # Change this to raise value error when using driver file?

    info = {'Description': ['Animal ID number', 'Date', 'Brief description'],
            'Data': [animal_num, exp_yyyy_mm_dd, exp_desc]}

    metadata_df = pd.DataFrame(info)
    metadata_df.to_csv(summarycsv_name, index=False)

    return metadata_df


def raw_signal_trace(fpho_dataframe):

    df = fpho_dataframe
    # print(df.head(1))

    # Get user input for what to plot
    channel_input = input("----------\n"
                          + "What channel(s) would you like to plot?\n"
                          + "\nOptions are f1Red, f2Red, f1Green, f2Green."
                          + "\n\nIf plotting multiple channels,"
                          + " please separate with a space or comma."
                          + "\n----------\n"
                          + "Selection: ")

    # Make a list of user input
    if ',' in channel_input:
        channel_list = channel_input.split(',')
    else:
        channel_list = channel_input.split(' ')

    # quick for loop to catch input error -- input not found in column names
    for channel in channel_list:
        col = df.columns.str.contains(pat=str(channel))
        if not any(col):
            print("Could not find entries for channels you'd like to plot"
                  + " in the dataframe column names."
                  + " You entered <" + channel + "> and the options are "
                  + str(list(df.columns)))
            print('Please restart...\n')
            sys.exit(1)

    # Replace user input with actual column name
    for channel in channel_list:

        if 'f1Red' in str(channel):
            title = channel
            channel = "f1RedRed"
            time_col = 'fTimeRed'
            l_color = "r"
        if 'f2Red' in str(channel):
            title = channel
            channel = "f2RedRed"
            time_col = 'fTimeRed'
            l_color = "r"
        if 'f1Green' in str(channel):
            title = channel
            channel = "f1GreenGreen"
            time_col = 'fTimeGreen'
            l_color = "g"
        if 'f2Green' in str(channel):
            title = channel
            channel = "f2GreenGreen"
            time_col = 'fTimeGreen'
            l_color = "g"

        channel_idx = df.columns.get_loc(channel)
        time_idx = df.columns.get_loc(time_col)

        plt.figure()
        plt.plot(df.iloc[:, time_idx], df.iloc[:, channel_idx], color=l_color)
        plt.title(str(title))

    print('\nClose plot window(s) to end script.')
    plt.show()
    return None


def plot_1fiber_norm_iso(fpho_dataframe):
    """Creates a plot normalizing 1 fiber data to the isosbestic

        Parameters
        ----------
        fpho_dataframe: string
                File containing dataframe

        Returns:
        --------
        f1GreenNorm.png and f1RedNorm.png: png file
                File containing the normalized plot for each fluorophore
    """

    # Open data frame
    # Check for FileNotFound and Permission Error exceptions
    try:
        f = open(fpho_dataframe, 'r',)
    except FileNotFoundError:
        print('No ' + fpho_dataframe + ' file found')
        sys.exit(1)
    except PermissionError:
        print('Unable to access file ' + fpho_dataframe)
        sys.exit(1)

    # Initialize vectors for the isosbectic data, fluorophore data
    # and time data
    f1GreenIso = []
    f1GreenGreen = []
    f1GreenTime = []

    f1RedIso = []
    f1RedRed = []
    f1RedTime = []

    # Assign columns
    greenIso_col = 0
    greenGreen_col = 2
    greenTime_col = 8
    redIso_col = 3
    redRed_col = 4
    redTime_col = 7

    # Read through each line of the dataframe
    # Append the isosbectic, fluorophore and time data to their
    # respective vectors, depending on color
    header = None
    for line in f:
        if header is None:
            header = line
            continue
        A = line.rstrip().split(',')
        f1GreenIso.append(float(A[greenIso_col]))
        f1GreenGreen.append(float(A[greenGreen_col]))
        f1GreenTime.append(float(A[greenTime_col]))
        f1RedIso.append(float(A[redIso_col]))
        f1RedRed.append(float(A[redRed_col]))
        f1RedTime.append(float(A[redTime_col]))

    # Get coefficients for normalized fit
    regGreen = np.polyfit(f1GreenIso, f1GreenGreen, 1)
    aGreen = regGreen[0]
    bGreen = regGreen[1]

    regRed = np.polyfit(f1RedIso, f1RedRed, 1)
    aRed = regRed[0]
    bRed = regRed[1]

    # Use the coefficients to create a control fit
    controlFitGreen = []
    for value in f1GreenIso:
        controlFitGreen.append(aGreen * value + bGreen)

    controlFitRed = []
    for value in f1RedIso:
        controlFitRed.append(aRed * value + bRed)

    # Normalize the fluorophore data using the control fit
    normDataGreen = []
    for i in range(len(f1GreenGreen)):
        normDataGreen.append((f1GreenGreen[i]
                              - controlFitGreen[i]) / controlFitGreen[i])

    normDataRed = []
    for i in range(len(f1RedRed)):
        normDataRed.append((f1RedRed[i] - controlFitRed[i]) / controlFitRed[i])

    # Plot the data for green
    plt.plot(f1GreenTime, normDataGreen)
    plt.title('Green Normalized to Isosbestic')

    # Save the plot in a png file
    figGreen = plt.savefig('f1GreenNormIso.png')
    plt.close(figGreen)

    # Plot the data for red
    plt.plot(f1RedTime, normDataRed)
    plt.title('Red Normalized to Isosbestic')

    # Save the plot in a png file
    figRed = plt.savefig('f1RedNormIso.png')
    plt.close(figRed)

    f.close()
