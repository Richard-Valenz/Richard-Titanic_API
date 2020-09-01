# Richard-Titanic_API

Welcome to the Titanic prediction API, this is a data science project which predicts the survival of a person given determined parameters based on a passenger's information.


## TASKS

### TASK1 - organizational instructions
 Create your own repository on Github or other public code versioning server. Use content of this project to create initial commit.
 
 Follow the rules:
* The solutions to all subsequnt tasks should be in your repository.
* Each task should be solved in separate branch using any number of commits. You can edit the code or add additional file explaining your way of thinking. The branch name should be related to the task, so we can know which branch applies to which task.
* All branches should finally be merged to master branch.
* At the end remember to share your repository with us.

#### Solution

  All branches and modifications have been properly set up in the repository. 

### TASK2 - sense of humour 🎭 

Add a file with your favourite joke to the docs directory.

#### Solution
  Favorite jokes located in ./source_code/doc/ folder 😊


### TASK3 - good practices 💯
* Correct the code so it is easy to read, run and reuse.
* Remember about
  * README.md files
  * Code comments
  * quality and performance of code -- remove or fix badly written code

#### Solution

  Two different folders have been created in order to give a good organization for both the source code and the api

### Installation 

#### Source code installation
Install the necessary python modules:

```sh
$ cd source_code
$ pip install -r requirements.txt
$ python run.py

```

#### Server-API installation

```sh
$ cd server
$ pip install -r requirements.txt
$ python app.py
```


### TASK4 - feature engineering 🔧
Propose better solution for feature engineering than the one given by us.

#### Solution

  Solution has been solved in build_features.py

### TASK5 - models 📊 
Propose other prediction models than the one proposed by us. 

#### Solution

  Solution has been solved in train.py

### TASK6 - measures 🎯
After completing TASK5, justify why you have chosen this particular model. Compare it with the model proposed by us or with any other model choosen by you. If you haven't completed TASK5, write theoretically how can you compare two solutions.

#### Solution

  Solution has been solved in run.py (output in terminal)

### TASK7 - docker 🐳
Prepare a Dockerfile that will allow us to run your code in the container.

#### Solution

  Solution has been solved in ./docker-compose.yml, ./server/Dockerfile


### TASK8 - tests ✅
Write unit tests covering your code.

#### Solution

  Solution has been solved in ./source_code/src/test_{file.py}

### TASK9 - prediction api 📡
Prepare a code that will share your model via API. It should be accessible by the HTTP protocol and accept and return data in JSON format

#### Solution


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


## Thank you so much for the opportunity. 
### Look forward to hearing from you !
