# CRUD example using Django and PostgreSQL

This repository shows an example of usage of the 
Django web framework using Python 3.7.3 and a
PostgreSQL relational database.

This example contains a server made to run locally. 
It shows initially whether there are available products 
(**Produtos**) or not, and after the additions of products it
allows the user to make an order. 

The user is allowed to create,  read, update, and delete both
orders and products if some criteria is met:
  
  + Products can be only deleted if there is no existing order using it;
  + Orders can be only made if there are enough products to do so.
  + If an order is updated, this update results in changes on the
    number of available products. Case it is deleted, it only takes effect
    if it has not ben sent (**"Pendente de envio"**).
  

## Setup

This setup is intended for **Unix-like** systems, but is
probably analogous for Windows systems.

### PostgreSQL setup

If you PostgreSQL already installed, head out to
https://www.postgresql.org
and download it.

After installing, open your database command line (tip)and create
the needed database named **store** with a user **postgres** 
(you can leave your own user and choose any name to the database, 
but you will need to change it on the Django afterwards). So:

```console
$ psql
# CREATE DATABASE store WITH OWNER=postgres;
```

You can see if it was create by using the command **\list**, but it is pretty much done.

### Python setup

 Start by installing  **virtualenv** via **pip**. It is used here to sandbox
 our Python. 
 
 ```console
 $ pip install virtualenv
 ```
 
 After that you head out to the folder of this repository on your computer and 
 will create the virtual environment (here named p3), it must be a Python3 
 (>=3.6). Afterwards, the virtualenv will be activated (** source p3/bin/activate **) 
 and  the dependencies  will be installed as well, so the next commands should do.
 
 ```console
 $ virtualenv p3 -p $(which python3)
 $ source p3/bin/activate
 (p3) $ pip install -r requirements.txt
 ```
 
 If for some reason it does not work, install the libraries needed manually from teh activated
 environment by:
 
 ``` console
 (p3) $ pip install django==2.2.5
 (p3) $ pip install psycopg2==2.8.3
 ```
By the way, this environment can be deactivated by simple typing **deactivate**.

### Django setup

From inside this project folder (same as previous) and with the virtualenv activated, 
type in your terminal (assuming you did everything as said previously):

```console
(p3) $ python manage.py makemigrations
(p3) $ python manage.py migrate
```

 If you decided to use your own database name, user, port, or even had a password on your PostgreSQL
 database, head out to the **settings.py** file  (inside the store folder) and edit the following
 field accordingly
 ```code
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<YOUR DATABASE NAME>',
        'USER': '<YOUR USERNAME>',
        'PASSWORD': '<YOUR PASSWORD>',
        'HOST': '<YOUR HOST ADDRESS>',
        'PORT': '<YOUR PORT>'
    }
}
 ```


Case you experience some error during the migrate, try dropping your database and creating a new one.

## Running

After completing the setup, it is quite easy to run, open
your terminal on the folder of this repository and run:

```console
$ source p3/bin/activate
(p3) $ python manage.py runserver
```
Now head out to your browser and  go to http://localhost:8000/ to use it.

You should see something like this:

![running](running.png)

You can start using it by adding some products and making some purchases.
