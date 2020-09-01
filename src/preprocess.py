import pandas as pd
import numpy as np

def execute(input_file, output_file):
    data = pd.read_csv(input_file, sep = ";")
    data = data.dropna()
    del(data["Name"])
    del(data["Ticket"])
    del(data["Cabin"])
    

    data.to_csv(output_file)
