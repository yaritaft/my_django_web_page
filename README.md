


## Table of Contents

- [Overview](#Overview)
- [PreRequisites](#PreRequisites)
- [Installation](#Installation)
- [How to run the APP](#how-to-run-the-app)
- [How to stop the APP](#how-to-stop-the-app)
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
<!--
 ### Test Coverage

**Build  in Travis**

[![Build Status](https://travis-ci.org/yaritaft/intive.svg?branch=master)](https://travis-ci.org/yaritaft/intive)

**Results in coveralls**

[![Coverage Status](https://coveralls.io/repos/github/yaritaft/intive/badge.svg)](https://coveralls.io/github/yaritaft/intive)

In order to reproduce test coverage follow these commands:

`pip install --trusted-host pypi.python.org -r requirements.txt`

`coverage run test.py`

`coverage report` 

 #### Results

![](https://github.com/yaritaft/intive/blob/master/images/coverage_report.PNG)
 -->

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