"""Library of functions for fpho_driver

    * import_fpho_data - saves data from csv in lists
    * make_summary_file - outputs txt file of summary info
    * plot_1fiber_norm_fitted - Plots 1 fiber normalized fitted exponenent
    * plot_2fiber_norm_fitted - Plots 2 fiber normalized fitted exponenent
    * plot_1fiber_norm_iso - Plots 1 fiber normalized isospestic fit
    * plot_2fiber_norm_iso - PLots 2 fiber normalized isospestic fit

"""
import sys
from statistics import mean

driver_version = 'v2.0'


def import_fpho_data(file_name):
    """Takes a file name, returns lists of parsed data

        Parameters
        ----------
        file_name: string
                The path to the CSV file

        Returns:
        --------
        fTime: float list
                A list containing time of the day in msec
        f1Red: float list
                A list containing red fluorescent values from first fiber
        f1Green: float list
                A list containing green fluorescent values from first fiber
        f2Red: float list
                A list containing red fluorescent values from second fiber
        f2Green: float list
                A list containing green fluorescent values from second fiber
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

    # De-interleave
    offset1 = f1Red[0::3]  # takes every 3rd element
    offset2 = f1Red[1::3]
    offset3 = f1Red[2::3]
    meanoffsets = [mean(offset1), mean(offset2), mean(offset3)]
    # Red signal has max mean
    redIdx = meanoffsets.index(max(meanoffsets))

    # Assigning correct rows to colors
    # First fiber, green
    f1GreenIso = f1Green[redIdx+2::3]    # iso
    f1GreenRed = f1Green[redIdx::3]      # red
    f1GreenGreen = f1Green[redIdx+1::3]  # green

    # First fiber, red
    f1RedIso = f1Red[redIdx+2::3]
    f1RedRed = f1Red[redIdx::3]
    f1RedGreen = f1Red[redIdx+1::3]

    # Sorting time by color
    fTimeIso = fTime[redIdx+2::3]
    fTimeRed = fTime[redIdx::3]
    fTimeGreen = fTime[redIdx+1::3]

    if twoFiber:
        # Second fiber, green
        f2GreenIso = f2Green[redIdx+2::3]
        f2GreenRed = f2Green[redIdx::3]
        f2GreenGreen = f2Green[redIdx+1::3]

        # Second fiber, red
        f2RedIso = f2Red[redIdx+2::3]
        f2RedRed = f2Red[redIdx::3]
        f2RedGreen = f2Red[redIdx+1::3]

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


def make_summary_file(animal_num, date, exp):
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


def plot_1fiber_norm_fitted(fTime, f1Red, f1Green):
    """Plots fiberpho signal normalized to fitted exponenet

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
        norm_fitted_exp: plot
                A plot of normalized signal
        """


def plot_2fiber_norm_fitted(fTime, f1Red, f1Green, f2Red, f2Green):
    """Plots fiberpho signal normalized to fitted exponenet

        Parameters
        ----------
        fTime: float list
                A list containing time of the day in msec
        f1Red: float list
                A list containing red fluorescent values from first fiber
        f1Green: float list
                A list containing green fluorescent values from first fiber
        f2Red: float list
                A list containing red fluorescent values from second fiber
        f2Green: float list
                A list containing green fluorescent values from second fiber

        Returns:
        --------
        norm_fitted_exp: plot
                A plot of normalized signal
        """


def plot_1fiber_norm_iso(fTime, f1Red, f1Green):
    """Plots fiberpho signal normalized to isospestic

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


def plot_2fiber_norm_iso(fTime, f1Red, f1Green, f2Red, f2Green):
    """Plots fiberpho signal normalized to isospestic

        Parameters
        ----------
        fTime: float list
                A list containing time of the day in msec
        f1Red: float list
                A list containing red fluorescent values from first fiber
        f1Green: float list
                A list containing green fluorescent values from first fiber
        f2Red: float list
                A list containing red fluorescent values from second fiber
        f2Green: float list
                A list containing green fluorescent values from second fiber

        Returns:
        --------
        norm_iso: plot
                A plot of normalized signal
        """

