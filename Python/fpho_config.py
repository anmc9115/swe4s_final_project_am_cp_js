"""This file runs the functions in the fpho_setup library"""
import argparse
import sys
import fpho_setup
import yaml
import behavior_setup
import pandas as pd


def main():
    """Runs functions in fpho_setup, asks for what analysis to perform

    Parameters
    ----------
    config.yml
        To use this driver, update the config.yml file, then
        run the following bash command: 
        python fpho_config.py --config config.yml
    
    Returns
    -------
    Pandas dataframe of parsed fiber photometry data
    Writes an output CSV to specified file name
    Outputs specified plots and analysis
    """
    # use with config.yml
    parser = argparse.ArgumentParser()

    parser.add_argument('--config', type=str, required=True)
    args = parser.parse_args()

    f = open(args.config, 'r')
    config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()

    # Generate the dataframe with data
    fpho_df = fpho_setup.import_fpho_data(input_filename=config['input_filename'],
                                          output_filename=config['output_filename'],
                                          animal_ID=config['animal_ID'],
                                          exp_date=config['exp_date'],
                                          exp_desc=config['exp_desc'])

    # Plot raw signal if specified in commandline
    if config['plot_raw_signal'] == True:
        fpho_setup.raw_signal_trace(fpho_df, config['output_filename'])

    # Prints isosbestic fit if specified
    if config['plot_iso_fit'] == True:
        fpho_setup.plot_1fiber_norm_iso(fpho_df)

    # Prints fitted exponent if specified
    if config['plot_fit_exp'] == True:
        fpho_setup.plot_1fiber_norm_fitted(fpho_df)
       
    # Imports behavior data if specified
    behaviorData = pd.DataFrame() 
    if config['import_behavior'] == True:
        behaviorData = behavior_setup.import_behavior_data(config['BORIS_file'],
                                                           config['timestamp_file'])

        
if __name__ == '__main__':
    main()
