from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import sklearn
import pickle as pkl
import numpy as np


app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Welcome to the Titanic API<h1>'


class Predict(Resource):
    def post(self):
        #Get the posted data
        postedData = request.get_json()

        #Read the data
        pclass = postedData["pclass"]
        sex = postedData["sex"]
        age = postedData["age"]
        sibsp = postedData["sibsp"]
        parch = postedData["parch"]
        fare = postedData["fare"]
        embarked = postedData["embarked"]
        family_sz = postedData["family_sz"]
        is_alone = postedData["is_alone"]
        model_name = postedData["model_name"]

        #Confirming all values
        input_lst = [pclass,sex,age,sibsp,parch,fare,embarked,family_sz, is_alone]
        if not input_lst:
            return jsonify({"status":301,"msg":"missing value"})
            
        #Converting dtypes
        pclass = int(pclass)
        sex = int(sex)
        age = int(age)
        sibsp = int(sibsp)
        parch = int(parch)
        fare = int(fare)
        embarked = int(embarked)
        family_sz = int(family_sz)
        is_alone = int(is_alone)

        #Defining our input for model
        model_input = np.array([input_lst])

        #Load the model
        model_unpickle = open("models/{name}_model.pkl"
        .format(name=model_name),'rb')
        model = pkl.load(model_unpickle)
        model_unpickle.close()

        #Predicting our input selection
        prediction = model.predict(model_input)

        
        #get some output
        if str(prediction) == "[1]":

            retJson = { 
                "status": 200,
                "response": True,
                "msg": "This person survived"
            }

            return jsonify(retJson)

        elif str(prediction) == "[0]":

            retJson = {
                "status": 200,
                "response": False,
                "msg": "This person did not survived"
            }

            return jsonify(retJson)

    def get(self):

        retJson = { 
            "status": 200,
            "response": "ok",
            "msg": "Welcome to the Titanic API"
        }

        return jsonify(retJson)


api.add_resource(Predict, '/predict')


if __name__ == "__main__":
    app.run(host='0.0.0.0')



