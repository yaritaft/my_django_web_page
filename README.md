


## Table of Contents

- [Overview](#Overview)
- [PreRequisites](#PreRequisites)
- [Installation](#Installation)
- [How to run the APP](#how-to-run-the-app)
- [How to stop the APP](#how-to-stop-the-app)
- [How to run db and app separated](#how-to-run-db-and-app-separated)
<!--- [Test Coverage](#test-coverage) -->
- [Technology](#Technology)
- [Programming Language](#programming-language)
- [Dependencies](#Dependencies)
- [Author](#Author)
- [Standards](#Standards)

### Overview

#### Context:

The idea of this repository is to show how my web was built and how can you
clone the repository in order to execute the APP and try it yourself.

### PreRequisites

- Python 3.8.0 installed.
- Pip 3 installed.
- Docker+Docker-composed installed and with non sudo need to execute dockerfiles.
(https://docs.docker.com/install/linux/linux-postinstall/)
- PostgreSQL NON installed (or at least not running as daemon)
- Linux is desirable because if you have that OS you can directly execute the 
.sh scripts and run the app very easily.

### Installation

Open a terminal with git installed:

`git clone https://github.com/yaritaft/my_django_web_page.git`

### How to run the APP

Warning: If you can't execute do chmod 777 over both sh files.

Inside the project's folder:

`./auto_test_run.sh`

If everything went right, you should see a result like this one:

![](https://github.com/yaritaft/my_django_web_page/blob/master/mysite/documentation/app_running.png)

The last thing you have to do is to:

Control + Right Click over the IP shown in the console.

### How to stop the APP

`./auto_test_shutdown.sh`

Warnings:

If you have another app running on port 8000 the APP wont be able to run.
If you have another app running on port 5432 postgresSQL wont be able to run.

### How to run db and app separated

If you want to execute the db and the app separately. For example, dockerized
DB with local app executing directly python manage.py.

Go to this folder: db_isolated_container_to_test

Then type:

`docker-compose up`

Now you will have a db up on host 0.0.0.0 with an exposed port of 5432.

Then you just need to return to the root folder and type:

`python manage.py runserver`

or

`gunicorn mysite.wsgi`

### Test Coverage

`coverage run test.py`

`coverage report` 

 #### Results

![](https://github.com/yaritaft/my_django_web_page/blob/master/mysite/documentation/test_coverage_1.png)

![](https://github.com/yaritaft/my_django_web_page/blob/master/mysite/documentation/test_coverage_2.png)

### Technology

#### Programming Language

Python version 3.8.0
Django version 3.0

#### Dependencies 

Dependencies can be found in requirements.txt.

### Standards

- Flake8
- PEP8 (with Black)

### Deployment

The cloud service selected was Heroku because of it's simplicity to code and
deploy quickly without setting a lot of things.

The whole app was dockerized. So it would be easy to deploy it in other cloud
services if it is necessary.

And the DB is a postgres SQL DB (non container in production).


### Author
Yari Ivan Taft

https://github.com/yaritaft/