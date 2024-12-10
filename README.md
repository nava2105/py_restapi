# py_restapi
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
## General Info
***
This is a project built in Python using Flask to provide a simple REST API that returns a "Hello World" message in JSON format.
## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org): Version 3.12.0
* [Flask](https://flask.palletsprojects.com/en/stable/): Version 3.1.0
- [Swagger](https://swagger.io/docs): Version 0.0.2
## Installation
***
There are two methods to install this project.
### Via GitHub
Verify you are python version 3.12.0
```
python --version
```
Copy the repository
```
git clone https://github.com/nava2105/py_restapi.git
```
Enter the directory
```
cd ../py_restapi
```
Create a virtual environment
```
python -m venv .venv
```
Activate your virtual environment
* In Windows
```
.venv\Scripts\activate
```
In macOS or Linux
```
source .venv/bin/activate
```
Build the dependencies
```
pip install -r requirements.txt
```
Run main.py file
* By using python command
```
python main.py
```
* If you are using Python 3 and python points to Python 2 on your system, use python3 instead:
```
python3 main.py
```
Open a browser and enter to
[http://localhost:5000](http://localhost:5000)


Or to review the endpoints in Swagger enter to
[http:localhost:5000/apidocs](http:localhost:5000/apidocs)
### Via Docker-hub
Pull the image from Docker-hub
```
docker pull na4va4/py_restapi
```
Start a container from the image
```
docker run -p 5000:5000 na4va4/py_restapi
```
Open a browser and enter to
[http://localhost:5000](http://localhost:5000)


Or to review the endpoints in Swagger enter to
[http:localhost:5000/apidocs](http:localhost:5000/apidocs)