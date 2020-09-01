import pandas as pd
import sklearn

def execute(input_file, output_file, force_write = True):
    """
    Extract and transform features from the dataset into formats suitable for the
    machine learning model.

    Args:
        input_file (str): dataset file location
        output_file (str): feature-engineered dataset file location
    """

    df = pd.read_csv(input_file)

    #Preparing Sex column (mapping)
    df.Sex = df["Sex"].map({'female':1, 'male':0})




















    #Preparing Embarked column (mapping)
    df.Embarked = df["Embarked"].map({'S':0, 'C':1, 'Q':2})
    
    #Adding FamilySize column
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    #Adding IsAlone column
    df["IsAlone"] = 0
    df.loc[df["FamilySize"] == 1, "IsAlone"] = 1


   






















    df.to_csv(output_file, index=False)