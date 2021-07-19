# Richard-Titanic_API

Welcome to the Titanic prediction API, this is a data science project which predicts the survival of a person given determined parameters based on a passenger's information.

# UPDATE 2021! : REST API service taken down

### Installation 

#### Source code installation
Install the necessary python modules:

```sh
$ cd source_code
$ pip install -r requirements.txt
$ cd src
$ python run.py

```

#### Server-API installation

```sh
$ cd server
$ pip install -r requirements.txt
$ python app.py
```


#### API Testing 

  Please find below the following url: 
```sh
Method          POST
Base            http://ec2-107-23-94-190.compute-1.amazonaws.com:5000/
EndPoint        /predict
Header
  Content-Type  application/json
Body
  parch         Integer
  sex           Boolean (1 or 0)
  sibsp         Integer
  parch         Integer
  fare          Range [0 to 3]
  embarked      Range [0 to 2]
  family_sz     Integer
  is_alone      Boolean (1 or 0)
  model_name    String  ['rfc','etc','gbc','ada']


```

  As a response you will get the following JSON response (depending on the prediction)

```sh
  {
    "msg": "This person survived",
    "response": true,
    "status": 200
  }
```
  or
```sh
  {
    "msg": "This person did not survived",
    "response": false,
    "status": 200
  }
```
