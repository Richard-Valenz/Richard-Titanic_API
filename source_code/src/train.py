import numpy as np
import pandas as pd
import sklearn
import pickle as pkl
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics

def execute():
    """
    Trains our data and saves the model in a pickle file

    Returns:
        Trainig model accuracy from train_bf.csv
    """

    # Split the data for training.
    df = pd.read_csv("../data/train_bf.csv") #OJO: incorrect path
    df.dropna()
    #Defining X and y
    y = df["Survived"]
    X = df.drop(labels=['Survived'], axis=1)

    # MODELS PREDICTION 

    # RandomForestClassifier
    rfc_clf = RandomForestClassifier(n_estimators=12, random_state=21)
    rfc_clf.fit(X,y)
    preds = rfc_clf.predict(X)
    rfc_result = metrics.accuracy_score(y,preds)

    #Saving the model
    rfc_model = open("../models/rfc_model.pkl", 'wb')
    pkl.dump(rfc_clf, rfc_model)
    rfc_model.close()





































    train_acc = [rfc_result]

    compare_models = pd.DataFrame({
        'Model': ['RandForest'],
        'Score': train_acc,

    })








    print("Training ready ! ")
    return train_acc
    



if __name__ == "__main__":
    execute()

