"""ADD DOCUMENTATION"""

import argparse
import sys
import fpho_setup

def main():
    """Runs functions in fpho_setup, asks for what analysis to perform
    
    Parameters
    ----------
    input_filename: string
            Name of input file containing fiber photometry data

    output_filename: string
            Name you'd like for the output CSV file. Should include 
            file path if different than current file
    animal_number: int
            Number of the animal corresponding to fluoresence data

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
    parser.add_argument('--animal_num',
                        dest='animal_num',
                        type=int,
                        required=False,                              # make required
                        help='Animal number for fluroesence data')
    parser.add_argument('--plot_raw_signal',
                        dest='plot_raw_signal',
                        type=bool,
                        required=False,
                        help='Type 1 to plot raw signal trace')
    parser.add_argument('--plot_iso_fit',
                        dest='plot_iso_fit',
                        type=bool,
                        required=False,
                        help='Type 1 to plot iso fitted trace')

    args = parser.parse_args()

    print(args.output_filename)

    fpho_df = fpho_setup.import_fpho_data(input_filename=args.input_filename,
                                          output_filename=args.output_filename)
    # prints raw signal
    if args.plot_raw_signal:
        fpho_setup.raw_signal_trace(fpho_df, args.output_filename)
    
    # prints isosbestic fit
    if args.plot_iso_fit:
        fpho_setup.plot_1fiber_norm_iso(fpho_df)
                               

if __name__ == '__main__':
    main()
