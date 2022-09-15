# Coding Challenge
A django app with RESTful API that get the minimum, maximum, average and median temperature for a given city and period of time.

## Installation
* Clone the project
```
$ git clone https://github.com/AMuriuki/yoyo-python-eng-test.git
```

* Navigate to project directory & initialize a virtual env
```
$ cd yoyo-python-eng-test
$ python3 -m venv venv
$ . venv/bin/activate
```

* Install dependencies 
```
$ pip install -r requirements.txt
```

* Sign-up for a free API key on [weatherapi](https://www.weatherapi.com/)

* Create `SECRET_KEY` for Django Settings
```
$ python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```

* Edit sample .env.example in `/weather/.env.example` and rename to `.env`
```
WEATHER_API_KEY=<YOUR-WEATHER-API-KEY>
SECRET_KEY=<YOUR-SECRET-KEY>
```
## Running a local instance
* Run tests
```
$ python manage.py test api
```
* Start up the server
```
$ python manage.py runserver
```
* Example API request:
```
localhost:8000/api/locations/London?days=3
``` 
