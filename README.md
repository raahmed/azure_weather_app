### Weather App

The weather appa basic example Django application that connects to CosmosDB, obtains data from Cosmos and displays it onto a front end.


### Installation Instructions
Clone the project.
``` $git clone https://github.com/raahmed/azure_weather_app```

cd intro the project directory
```$ cd azure_weather_app```

Create a new virtual environment using Python 3.7 and activate it.
```
$ python3 -m venv env
$ source env/bin/activate
```

Install dependencies from requirements.txt from within the virtual environment:
```
(env)$ pip install -r requirements.txt
```

Create a .env file in the repository and set it up to include the following information:
```
$ DJANGO_SECRET_KEY="somestring"
$ COSMOSDB_HOST="your_cosmosdb_hostname"
$ COSMOSDB_MASTER_KEY="your_cosmosdb_masterkey"
```

Run the local project by running the following within the virtual environment:
```
(env) $ python manage.py runserver
```
