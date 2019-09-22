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

# Apply migrations
In order for the app to have the latest schema for the data, don't forget to apply migrations using the following command:
```shell
$ python manage.py migrate
```

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

# Generating new migration files
In case you've changed your schema recently, you should probably generate new migrations for the data
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```


