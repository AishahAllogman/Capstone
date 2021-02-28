## if you want to working with application locally 
#Installing Dependencies
**1. Python 3.7**
    Follow instructions to install the latest version of python for your platform in the python docs
**2.Virtual Enviornment**
    We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized.         Instructions for setting up a virual enviornment for your platform can be found in the python docs
**3. install all requirements**
    ```
    pip3 install -r requirements.txt
    ```
    This will install all of the required packages we selected within the requirements.txt file.
**4-environment variables**
Refer to the setup.sh file and export the environment variables for the project.
**5-create database**
create local database and export the database URI as an environment variable with the key DATABASE_URL.
**6-Database Migrations**
```
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```
***7-Run the Flask**
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
