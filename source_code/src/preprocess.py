import pandas as pd
import numpy as np

def execute(input_file, output_file):
     """
    Cleans and preprocess first filter from dataset

    Args:
        input_file (str): dataset file location
        output_file (str): preprocessed dataset file location
    """
    #Load dataset
    data = pd.read_csv(input_file, sep = ";")
    data = data.dropna()
    #Drop unnecessary columns
    drop_cols = ['Name','Ticket','Cabin','PassengerId']
    data = data.drop(labels=drop_cols, axis=1)

    #Save the dataset
    data.to_csv(output_file, index=False)
