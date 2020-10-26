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


def import_fpho_data(input_filename, output_filename):
    """Takes a file name, return a dataframe of parsed data

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
    fiber_val = int(input("One fiber or two fiber input data?\n"
                          + "Please enter 1 if one fiber "
                          + "or 2 if two fiber:\n"))
    while fiber_val not in [1, 2]:
        print("Your input for the # of fibers in input data was invalid.\n"
              + "Please enter either 1 or 2 as an integer.")
        sys.exit(1)

    f1Red_col = int(input("Which column contains f1Red information?\n"
                          + "Please enter 3 or 4 as an integer:\n"))
    while f1Red_col not in [3, 4]:
        print("Your input", f1Red_col, "is invalid.\n",
              "Please enter either 3 or 4, or 'x' to exit.\n")
        f1Red_col = input("Which column contains f1Red information?\n",
                          "Please enter 3 or 4 as an integer:\n")
        if f1Red_col == 'x':
            exit()

    if f1Red_col == 3:
        f1Green_col = 4
        while True:
            answer = input("You indicated that column 3 contains F1 red"
                           + " and column 4 contains F1 green. "
                           + "Is this correct (yes or no)?\n")
            if answer.lower().startswith("y"):
                print("ok, carry on then\n")
                break
            elif answer.lower().startswith("n"):
                print("You replied no. Restarting data information entry")
                exit()
    else:
        f1Green_col = 3
        while True:
            answer = input("You indicated that column 3 contains F1 green"
                           + " and column 4 contains F1 red. "
                           + "Is this correct (yes or no)?\n")
            if answer.lower().startswith("y"):
                print("ok, carry on then\n")
                break
            elif answer.lower().startswith("n"):
                print("You replied no. Please restart")
                exit()

    if fiber_val == 2:
        f2Red_col = int(input("Which column contains f2Red information?\n"
                              + "Please enter 5 or 6 as an integer:\n"))
        while f2Red_col not in [4, 5]:
            print("Your input", f2Red_col,
                  "is invalid.\nPlease enter either 5 or 6, or 'x' to exit.\n")
            f2Red_col = input("Which column contains f2Red information?\n"
                              + "Please enter 5 or 6 as an integer:\n")
            if f2Red_col == 'x':
                exit()

        if f2Red_col == 5:
            f2Green_col = 6
            while True:
                answer = input("You indicated that column 5 contains F2 red "
                               + "and column 6 contains F2 green. "
                               + "Is this correct (yes or no)?\n")
                if answer.lower().startswith("y"):
                    print("ok, carry on then\n")
                    break
                elif answer.lower().startswith("n"):
                    print("You replied no. Please restart")
                    exit()
        else:
            f2Green_col = 5
            while True:
                answer = input("You indicated that column 5 contains F2 green "
                               + "and column 6 contains F2 red. "
                               + "Is this correct (yes or no)?\n")
                if answer.lower().startswith("y"):
                    print("ok, carry on then\n")
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
    # print(len(f1Green),len(f1Red),len(f2Green), len(f2Red), len(fTime))

    # De-interleave
    offset1 = f1Green[0::3]  # takes every 3rd element
    offset2 = f1Green[1::3]
    offset3 = f1Green[2::3]
    meanoffsets = [mean(offset1), mean(offset2), mean(offset3)]
    # print(meanoffsets)

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

        twofiber_fdata = pd.DataFrame({'f1GreenIso': f1GreenIso,
                                       'f1GreenRed': f1GreenRed,
                                       'f1GreenGreen': f1GreenGreen,
                                       'f2GreenIso': f2GreenIso,
                                       'f2GreenRed': f2GreenRed,
                                       'f2GreenGreen': f2GreenGreen,
                                       'f1RedIso': f1RedIso,
                                       'f1RedRed': f1RedRed,
                                       'f1RedGreen': f1RedGreen,
                                       'f2RedIso': f2RedIso,
                                       'f2RedRed': f2RedRed,
                                       'f2RedGreen': f2RedGreen,
                                       'fTimeIso': fTimeIso,
                                       'fTimeRed': fTimeRed,
                                       'fTimeGreen': fTimeGreen})
        twofiber_fdata.to_csv(output_filename, index=False)
        return twofiber_fdata

    else:
        onefiber_fdata = pd.DataFrame({'f1GreenIso': f1GreenIso,
                                       'f1GreenRed': f1GreenRed,
                                       'f1GreenGreen': f1GreenGreen,
                                       'f1RedIso': f1RedIso,
                                       'f1RedRed': f1RedRed,
                                       'f1RedGreen': f1RedGreen,
                                       'fTimeIso': fTimeIso,
                                       'fTimeRed': fTimeRed,
                                       'fTimeGreen': fTimeGreen})
        onefiber_fdata.to_csv(output_filename, index=False)
        return onefiber_fdata
