


## Table of Contents

- [Overview](#Overview)
- [PreRequisites](#PreRequisites)
- [Installation](#Installation)
- [How to run the APP](#how-to-run-the-app)
- [Test Coverage](#test-coverage)
- [Technology](#Technology)
- [Programming Language](#programming-language)
- [Dependencies](#Dependencies)
- [Author](#Author)
- [Standards](#Standards)

### Overview

#### Context:

The idea of this repository is to show how my web is built.

Tests and furthers features will be added.

### PreRequisites

Python 3.8.0 installed.
Pip 3 installed.
Docker installed and with non sudo need to execute dockerfiles.
PostgreSQL installed on your computer.

### Installation

Open a terminal with git installed:

`git clone https://github.com/yaritaft/my_django_web_page.git`

### How to run the APP

Inside the project's folder:

To build the image:

`docker build -t my_web_django_app .`

Then you can run it by typing:

`docker run --network host my_web_django_app`

You should see this in your console:

![](https://github.com/yaritaft/my_django_web_page/blob/master/documentation/app_running.png)

Then control + right click on 127.0.0.1:8000 and you will be able to see the
web app running.

Warnings:

If you have another app running on port 8000 the APP wont be able to run.
If you have another app running on port 5432 postgresSQL wont be able to run.

 ### Test Coverage

**Build  in Travis**

[![Build Status](https://travis-ci.org/yaritaft/intive.svg?branch=master)](https://travis-ci.org/yaritaft/intive)

**Results in coveralls**

[![Coverage Status](https://coveralls.io/repos/github/yaritaft/intive/badge.svg)](https://coveralls.io/github/yaritaft/intive)

In order to reproduce test coverage follow these commands:

`pip install --trusted-host pypi.python.org -r requirements.txt`

`coverage run test.py`

`coverage report` -->

<!-- #### Results

![](https://github.com/yaritaft/intive/blob/master/images/coverage_report.PNG)
 -->

### Technology

#### Programming Language

Python version 3.8.0
Django version 3.0

#### Dependencies 

Dependencies can also be found in requirements.txt.

### Standards

- Flake8
- PEP8 (with Black)

### Deployment

The cloud service selected was Heroku because of it's simplicity to code and
deploy quickly without setting a lot of things.

The whole app was dockerized. So it would be easy to deploy it in other cloud
services if it is necessary.

And the DB is a postgres SQL DB (non container).


### Author
Yari Ivan Taft

https://github.com/yaritaft/