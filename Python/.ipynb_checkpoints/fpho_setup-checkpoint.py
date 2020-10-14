"""Library of functions for fpho_driver

    * import_fpho_data - saves data from csv in lists
    * make_summary_file - outputs txt file of summary info
    * plot_1fiber_norm_fitted - outputs 1 fiber normalized plot, fitted exponenent
    * plot_2fiber_norm_fitted - outputs 2 fiber normalized plot, fitted exponenent
    * plot_1fiber_norm_iso - outputs 1 fiber normalized plot, isospestic fit
    * plot_2fiber_norm_iso - outputs 2 fiber normalized plot, isospestic fit

"""
import sys

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
        fTime.append(columns[0])
        f1Red.append(columns[2])
        f1Green.append(columns[3])
        if columns[4] and columns[5] is not None:
            f2Red.append(columns[4])
            f2Green.append(columns[5])
            twoFiber = True

    file.close()

    if twoFiber:
        return fTime, f1Red, f1Green, f2Red, f2Green

    return fTime, f1Red, f1Green

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
