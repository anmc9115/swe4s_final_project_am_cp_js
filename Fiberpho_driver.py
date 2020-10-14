"""Driver for Fiber Photometry Analysis
    
    * function_name - what it does

"""
import sys

driver_version = 'v2.0'

def import_fiberpho_data(file_name):
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

    for line in file:
        columns = line.rstrip().split(',')
        fTime.append(columns[0])
        f1Red.append(columns[2])
        f1Green.append(columns[3])
        if columns[4] is not None:
            f2Red.append(columns[4])
            f2Green.append(columns[5])
            return fTime, f1Red, f1Green, f2Red, f2Green
        
        return fTime, f1Red, f1Green

    
