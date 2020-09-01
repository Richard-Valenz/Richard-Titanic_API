import pandas as pd
import pickle as pkl
from sklearn import metrics
import numpy as np

def execute():

    """
    Predicts our data and saves the model in a pickle file

    Returns:
        Test model accuracy from val_bf.csv
    """
    df = pd.read_csv("../data/val_bf.csv")# OJO: incorrect path

    df.dropna(inplace = True)
    #Defining our target to be predicted
    target = df["Survived"]
    #Define your input data
    X = df.drop(labels=['Survived'], axis=1)
    
    models_lst = ['rfc','etc','gbc','ada'] #list of models name
    acc_lst = []

    # Models creations
    for i in models_lst:
        model_unpickle = open("../models/{name}_model.pkl".format(name=i), 'rb')
        model = pkl.load(model_unpickle)
        model_unpickle.close()
        predictions = model.predict(X)
        df["prediction"] = predictions
        df["target"] = target
        accuracy = metrics.accuracy_score(target,predictions)
        acc_lst.append(accuracy)

    compare_models = pd.DataFrame({
        'Model' : ['RandForest'],
        'Score' : acc_lst
    })
    #print(acc_lst)
    print("Predictions ready !")
    return acc_lst

if __name__ == "__main__":
    execute()

