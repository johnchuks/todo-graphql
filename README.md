### TODO APPLICATION ###


#### INTRODUCTION ####

This is a simple Todo API built with Graphene (graphQL framework for python) and python flask.


#### Getting Started ####
* Clone the repository with ``` git clone https://github.com/johnchuks/todo-graphql ```
* Install json web server globally like so ```npm install json-server -g```.
* Enter into the directory and `npm install` to install the javascript dependencies
* Create a virtual environment like so ``` virtualenv (name of env) ```
* Activate the virtual environment with ``` source (name of env)/bin/activate ```
* Enter the `todo-flask-app` directory.
* Install all the requirements like so ``` pip install -r requirements.txt ```
* export your application with ``` export FLASK_APP=app.py```
* export the json web server URL like so ``` export DB_URL=http://localhost:3000 ```.
* In the same terminal run ``` flask run ```
* Open a new terminal and cd into ``` todo-Graphql ``` and run ```json-server --watch db.json```.
* If you decide to the change port number for the json web server, use ```json-server --watch db.json --port (new port number)```.
* Then export the new URL as shown previously.
* To test the application enter in your browser this url ```http://localhost:5000/graphql```

