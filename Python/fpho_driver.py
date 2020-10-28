"""ADD DOCUMENTATION"""

import argparse
import sys
import fpho_setup_dataframes

def main():
    """Uses function(s) in fpho to....ADD DOCUMENTATION
    
    Parameters
    ----------
    input_filename: string
                    name of input file containing fiber photometry data

    output_filename: string
                     Name you'd like for the output CSV file. Should include 
                     file path if different than current file


    Returns
    -------
    Pandas dataframe of parsed fiber photometry data

    Writes an output CSV to specified file name
    """

    parser = argparse.ArgumentParser(description= ('Parse fiber photometry data'
                                                  +'to prepare for analyses'))

    parser.add_argument('--input_filename',
                        dest='input_filename',
                        type=str,
                        required=True,
                        help='Name of input file as string')

    parser.add_argument('--output_filename',
                        dest='output_filename',
                        type=str,
                        required=True,
                        help='Name for output file as string')

    args = parser.parse_args()

    # Run import_fpho_data. I think this will always happen, and then we may do
    # different things with this data, which will be optional arguments. If so,
    # should we also return a dataframe?

    print(args.output_filename)

    fpho_df = fpho_setup_dataframes.import_fpho_data(input_filename=args.input_filename,
                                                     output_filename=args.output_filename)

    # print(fpho_df)                                                 

if __name__ == '__main__':
    main()
