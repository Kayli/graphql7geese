# Prerequesites: 
- python 3.7.x
- pip
- virtualenv

# Initialization
- run python virtual environment initialization script:
```shell
$ source ./create-virtualenv.sh
```
This will initialize virtual environment and pip install required dependencies from requirements.txt needed for the project.

- activate virtual environment by running the following script: 
```shell
$ .env/bin/activate
```
This will make sure that your application is using correct version of python and all required dependencies.

# Running tests
```shell
$ python manage.py test
```

# Running django dev server
```shell
$ python manage.py runserver
```

# Re-seeding data
```shell
$ python manage.py loaddata seed.yaml
```

# Generating and running migrations
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```


