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

    # ExtraTreesClassifier
    etc_clf = ExtraTreesClassifier(n_estimators=15)
    etc_clf.fit(X,y)
    preds = etc_clf.predict(X)
    etc_result = metrics.accuracy_score(y,preds)

    #Saving the model
    etc_model = open("../models/etc_model.pkl", 'wb')
    pkl.dump(etc_clf, etc_model)
    etc_model.close()


    # GradientBoosringClassifier
    gbc_clf = GradientBoostingClassifier(n_estimators=20)#82 78
    gbc_clf.fit(X,y)
    preds = gbc_clf.predict(X)
    gbc_result = metrics.accuracy_score(y,preds)

    #Saving the model
    gbc_model = open("../models/gbc_model.pkl", 'wb')
    pkl.dump(gbc_clf, gbc_model)
    gbc_model.close()


    # AdaBoostClassifier
    ada_clf = AdaBoostClassifier(n_estimators=12) # 73 85
    ada_clf.fit(X,y)
    preds = ada_clf.predict(X)
    ada_result = metrics.accuracy_score(y,preds)

    #Saving the model
    ada_model = open("../models/ada_model.pkl","wb")
    pkl.dump(ada_clf, ada_model)
    ada_model.close()

    train_acc = [rfc_result, etc_result, gbc_result, ada_result]

    compare_models = pd.DataFrame({
        'Model': ['RandForest','ExtTree', 'GraBoo', 'AdaBoo'],
        'Score': train_acc,

    })


    





    print("Training ready ! ")
    return train_acc
    



if __name__ == "__main__":
    execute()

