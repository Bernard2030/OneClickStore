# One Click Store Backend

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

[![OnlineStore Django Application](https://github.com/Bernard2030/OneClickStore/actions/workflows/django-online-store.yml/badge.svg)](https://github.com/Bernard2030/OneClickStore/actions/workflows/django-online-store.yml)

[![Docker Compose Actions Workflow](https://github.com/Bernard2030/OneClickStore/actions/workflows/online-store-docker.yml/badge.svg)](https://github.com/Bernard2030/OneClickStore/actions/workflows/online-store-docker.yml)

Nowadays getting good quality used items at a fair price is becoming hectic, and even very difficult to
get some items like used vehicles even in national Auction centres. On the other hand is how some of these goods can be able to reach their intended new owners in time and in good quality.

The application will bridge the gap and ensure availability of the products to the intended recipients
in time.
It will also create an avenue for users to also sell their items which they no longer need through
the website.

## User Stories 
* A user is able to sign up and set up their own profile
* A user can search required products, and it should return product and its category.
* A user should check out to the payment page and make payments.
* A user should know the expected time of  product arrival through both email and normal text.
* A user should know the mode of transportation and details of the person in charge of delivering the product.
* A user MUST be able to sell used items to the company if the user has any.
* The company MUST be able to decide to buy based on the images sent by the user.
* A user can post bids on a product.
* A user can view the bids on a product.

# Architecture Overview 
The API serves a backend to the Ecommerce found [here](https://github.com/indomitable-core/E-commerce). The frontend is built 
in Angular and the backend is built in Django. 

Overview of the architecture: 

![Architecture](media/Architure.drawio.png)

Overview of the devops and dashboard implementation: 

![Architecture](media/devops.drawio.png)

## API Endpoints
   You should create an API so that users and the frontend can access data from your application.:

    - `/api/products`
    - `/api/products/<product_id>`
    - `/api/login`
    - `/api/register`
    - `/api/refresh-token` 
    - `/api/users/<user_id>`
    - `/api/users/<user_id>/products`
    - `/api/users/<user_id>/products/<product_id>`

# Link to Deployed application

[![Deployed Application](https://img.shields.io/badge/Deployed-Application-green.svg)](https://backend-store-api.herokuapp.com/api/)

Check live API --> [Here](https://backend-store-api.herokuapp.com/api/)

## Documentation on the API

[![Documentation](https://img.shields.io/badge/Documentation-API-blue.svg)](https://backend-store-api.herokuapp.com/api-docs/)

View docs [Here](https://backend-store-api.herokuapp.com/api-docs/)


# Setup Instructions / Installation

### Getting Started

### Prerequisites

- Python and pip (I am currently using 3.9.7) Any version above 3.7 should work.
* Git installed on your machine
* Code editor/ IDE
* PostgreSQL installed on your machine

### Installation and Running the App

1. Clone GitHub repository

    ```shell
    git clone https://github.com/Bernard2030/OneClickStore
    ```

2. Change into the folder

    ```shell
   cd OneClickStore
    ```

3. Create a virtual environment

   ```shell
      python3 -m venv venv 
   ```

    * Activate the virtual environment

   ```shell
   source ./bin/activate
   ```

* If you are using [pyenv](https://github.com/pyenv/pyenv):

  3a. Create a virtualenv

   ```
       pyenv virtualenv OneClickStore
   ```

  3b. Activate the virtualenv

   ```
   pyenv activate OneClickStore
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

   OR Copy the included example

    ```
    cp .env-example .env 
    ```

5. Add your credentials to the `.env` file
    
    OR
   ```
   export DATABASE_URL=postgres://username:password@localhost:5432/database_name
   ```

6. Migrate your database
    ```shell
    python manage.py migrate
    ```

7. Install the required dependencies

   ```shell
   pip install -r requirements.txt
   ```

8. Make the shell script executable

    ```shell
   chmod a+x ./run.sh
    ```

9. Run the app

    ```shell
   ./run.sh
    ```

   OR
   run with python

    ```shell
   python manage.py runserver
    ```

## Tests

* To run the tests:

    ```shell
  python manage.py test
    ```

## API endpoints



## Technologies used

* Python-3.9.7
* Django web framework
* PostgreSQL
* Insomnia
* Heroku
* Sendgrid

## LICENSE 
MIT License

Copyright (c) 2021 Bernard Opiyo && Kennedy Ngugi Mwaura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: