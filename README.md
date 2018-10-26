[![Maintainability](https://api.codeclimate.com/v1/badges/481c31379b0b3a8b90df/maintainability)](https://codeclimate.com/github/CandySusan/Store-Manager/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/CandySusan/Store-Manager/badge.svg?branch=master)](https://coveralls.io/github/CandySusan/Store-Manager?branch=master)
[![Build Status](https://travis-ci.org/CandySusan/Store-Manager.svg?branch=develop)](https://travis-ci.org/CandySusan/Store-Manager)

My Store Manager API endpoints
**************************************************
This is a set of API endpoints already defined below and uses data structures to store data in memory.
Store Manager Api endpoints doesn't have a database.

Project
********************************************************
To run the project Locally, clone [https://github.com/CandySusan/Store-Manager/tree/develop]

. cd into the folder that contains the cloned project.
. create a virtual environment.
. activate the virtual environment.
. pip install the requirements.txt.
. to run the project use python3. the run command is [python run.py].
. To access and use the application's endpoints on Postman, Use the following URL [https://store-manager-candy.herokuapp.com/]

Application Features

EndPoint	Function
POST /products	Create a new product
GET /products	Get all availabe products
GET /products/productId	Get a specific product given its ID
POST /sales	Create a new sales order record
GET /sales	Get all available sale records
GET /sale/saleId	Get a specific sale record given its ID

Installation & Requirements;
*******************************************************
Python

Flask (Python web framework)The following packages are optional:

Markdown (optional) - Markdown support for the browsable API. 

Pytest[Testing Framework]

Install using pip: pip install Flask 

Import and initialization of my application:
*********************************************

from flask import Flask

app = Flask(__name__)

Setup Development Environment 

Install Python
Install Pip
Install VirtualEnv

Running the tests

- Run pytest on the terminal to check for errors
- And also use the profeesional tool postman

Deployment

My app endpoints is hosted on heroku [https://store-manager-candy.herokuapp.com]

An example on how to Use the endpoints
******************************************************************
Creat a new product

Open postman and perform a POST request on [https://store-manager-candy.herokuapp.com/api/v1/products]
Data should be in json format, e.g -{"product_id":1,"product_name":"bags","product_price":56,"quantity":10}  
Note:
- All fields sould be filled for successful creation of a new product

Get all available Products

Perform a GET request on [https://store-manager-candy.herokuapp.com/api/v1/products]

Get a specific product by product_id

Perform a GET request and add product_id as shown [https://store-manager-candy.herokuapp.com/api/v1/products/2]

Note:
- Product_id is an integer and not a string so error message will be returned if string is entered instead.

Acknowledgments
- Used this URL as a guideline to build the api endpoints [http://flask.pocoo.org/]
- Also used Stackoverflow to guide during building of api endpoints

Authors

Candy Susan
