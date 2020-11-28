# Django-School-Management
A fullstack school management project in django, bootstrap-4 and javascript.

# Installation:
1. go to the project folder
2. run `pipenv install`
3. create `.env` under config folder and give credentials following `.env.example` template
3.1. See additional resources section to setup/get more info.
4. run `python manage.py migrate`
5. then `python manage.py runserver`
for testing, create a superuser too.

# Celery-redis setup:
1. Celery is installed, install redis as well. <br>
2. for linux users: 
- run redis server with `redis-server` command.
3. for windows users:
- Download redis (https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504)
- Run redis-server.exe and redis-cli.exe.

And finally, while django server is running, run this command on another terminal <br>
`celery -A config worker -l INFO`

# Additional Resources:
+ Create braintree sandbox account from: https://sandbox.braintreegateway.com/login

# Usage/testing
In order to test this project with dummy data:

* `populate_department` script to create departments
* create an academic session object from admin or dashboard
* populate_teachers
* populate_students

then for result, subjects, combinations you can run your script or just 
create data manually for now.

* APPLY CARD INFO AT `admission` link
`card number: 5555555555554444`
`expiracy: any valid future date` 
