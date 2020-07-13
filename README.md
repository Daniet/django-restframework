# Django rest framework example

## requirements
- python 3.8
- pipenv or virtualenv

## create enviroment
### virtuaenv
``` bash
virtualenv venv
# linux or mac
source venv/bin/activate
# windows
venv\Scripts\activate
# install depences
pip install -r requirements.txt
```
### pipenv
``` bash
pipenv shell
# install depences
pipenv install
```

### Migration
``` bash
python manager migration
```

## execute project
``` bash
python manager runserver 0:8000
```

[service django](http:127.0.0.0:8000)