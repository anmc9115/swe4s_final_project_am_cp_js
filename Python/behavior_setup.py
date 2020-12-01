import sys
from statistics import mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_behavior_data(animal_ID, exp_date, exp_desc,
                         input_filename, output_filename):
    """Takes a file name, returns a dataframe of parsed data

        Parameters
        ----------
        input_filename: string
                        The path to the CSV file

        output_filename: string
                         file path and name for output csv

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

def plot_zscore()