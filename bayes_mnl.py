import numpy as np 
import pandas as pd 
import pymc as pm 

# ------------ DATA PREP -------------

prepped_filename = "mt_ce_data"
raw_filename = "IS1326_ce_data_BIOGEME_updated" # sent from Jason Soria, cleaned stated choice experiment in Israel 

def prep_data(prepped_filename):
    try:
        return pd.read_csv(f"bayes_data/{prepped_filename}.csv")
    except:
        print("Data file has not been prepared. Importing raw data file...")
        raw = import_data()
        # TODO: prepare/clean the data here, if needed
        print("Cleaned file has been saved do bayes_data directory")
        raw.to_csv(f"bayes_data/{prepped_filename}.csv")

def import_data(raw_filename):
    data = pd.read_csv(f"bayes_data/{raw_filename}.csv")
    return data

