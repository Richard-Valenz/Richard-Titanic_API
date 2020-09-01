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

    #Preparing Age column
    age_lst = []

    for i in df["Age"]:
        #Grouping Age by stages of human development
        if i <= 17:
            i = 0
            age_lst.append(i)
        elif i > 17 and i <= 25:
            i = 1
            age_lst.append(i)
        elif i > 25 and i <= 50:
            i = 2
            age_lst.append(i)
        elif i > 50:
            i = 3
            age_lst.append(i)
    df["Age"] = age_lst

    #Preparing Embarked column (mapping)
    df.Embarked = df["Embarked"].map({'S':0, 'C':1, 'Q':2})

    #Adding FamilySize column
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    #Adding IsAlone column
    df["IsAlone"] = 0
    df.loc[df["FamilySize"] == 1, "IsAlone"] = 1

    #Rounding Fare column
    for i in df.Fare:
        i = round(i)
    #Grouping fare values
    fare_lst = []
    for i in df["Fare"]:

        if i <= 7.9:
            i = 0
            fare_lst.append(i)
        elif i > 7.9 and i <= 14.454:
            i = 1
            fare_lst.append(i)
        elif i > 14.454 and i <= 30.924:
            i = 2
            fare_lst.append(i)
        elif i >= 31:
            i = 3
            fare_lst.append(i)


    df['Fare'] = fare_lst
    df.Fare = df["Fare"].astype("int")

    df.to_csv(output_file, index=False)