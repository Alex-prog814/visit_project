#Visit Project

####Quick Start Guide

1. Setting up a virtual environment

    After cloning the project, go to the project folder using the terminal and type the following command:
    
    ```
    python3 -m venv venv
    ```
    
    now activate the environment:
    
    ```
    source venv/bin/activate
    ```

2. Django must be installed, along with all required modules and third-party libraries
    
    Type the following command:
    
    ```
   pip3 install -r requirements.txt
   ```
   
3. Need to create a database for the application
    
    Type the following command in the terminal:
    
    ```
   psql postgres
   CREATE DATABASE visit_project_db;
   \q
   ```
   
4. You need to create an .env file at the level of the manage.py file in which put the following data
    
    ```
   SECRET_KEY=you can generate new secret django project key on: https://djecrety.ir/
   DB_NAME=visit_project_db;
   DB_USER=type your username from psql here
   DB_PASSWORD=type your password from psql's user
   ```
   
5. Migrations to the database

    Type the command in the terminal:
    
    ```
   python3 manage.py makemigrations
   ```
   
   then
   
   ```
    python3 manage.py migrate
    ```
   
6. Create superuser

    Enter the following command to create a superuser:
    
    ```
   python3 manage.py createsuperuser
   ```
    
    then enter the requested data

    
7. Server start

    Enter the following command in terminal:
    
    ```
   python3 manage.py runserver
   ```   
   
8. After running the application, you can read the documentation at: http://127.0.0.1:8000/swagger/

    Fine! Project is ready to use.
