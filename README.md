# Donaldson Lab Fiberphotometry Analysis
> This project is for performing analysis on animal fiberphotemetry and behavior data 

In order to use this code you must have collected fiberphotometry data and behavior data using the behavior coding software BORIS (https://boris.readthedocs.io/en/latest/#behavioral-observation-research-interactive-software-boris-user-guide). 

## Installation

OS X & Linux:

```sh
git clone https://github.com/anmc9115/swe4s_final_project_am_cp_js.git
```

## To Use the Code
1. Obtain fiberphotometry data (msec/day) 
2. Score behavior using BORIS with the events recorded in `seconds`
3. Download raw data from behavior scoring using BORIS by clicking: `observations -> export events -> tabular events -> select observations -> save as csv`
4. Download all analysis software as described above
5. In the command line, navigate to the directory containing the code files and data
6. Edit the `config.ymal` file with the parameters specific to your experiment
7. In the command line, run the following command to execute the code:
      `python fpho_config.py --config config.yml`
8. A summary CSV along with any plots from analysis will be output to the working directory

## Example Plots
### Raw Signal Trace

### Normalized Signal to Isosbestic

### Normalized Signal to Biexponential Fit

### Z-score Plot for Behavior 

## Release History

* v1.0
