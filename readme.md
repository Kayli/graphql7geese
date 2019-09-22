# Prerequesites
In order to run the project successfully make sure you have installed the following components on your machine:
- python 3.7.x
- pip
- virtualenv

# Environment initialization
Run python virtual environment initialization script:
```shell
$ source ./create-virtualenv.sh
```
This will initialize virtual environment and pip install required dependencies from requirements.txt needed for the project.



# Running the project
## Virtual environment activation
Activate virtual environment by running the following script: 
```shell
$ .env/bin/activate
```
This will make sure that your application is using correct version of python and all required dependencies.
## Apply migrations
In order for the app to have the latest schema for the data, don't forget to apply migrations using the following command:
```shell
$ python manage.py migrate
```

## Running tests
Before running application server, it may be useful to make sure that all tests are passing by running the following command:
```shell
$ python manage.py test
```

## Running django dev server
This command will run webserver with django application:
```shell
$ python manage.py runserver
```

# Other useful commands 
## Re-seeding data
```shell
$ python manage.py loaddata seed.yaml
```

## Generating new migration files
In case you've changed your schema recently, you should probably generate new migrations for the data
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```


