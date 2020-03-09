# Dagram
A Django based web application looking to replicate instagram functionalities

## Features
- Django 3.0+
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.

## Environment Variables
```SECRET_KEY=XXX
DEBUG=True
DB_NAME='dagram'
DB_USER='don'
DB_PASSWORD='XXXX
DB_HOST='127.0.0.1'
MODE='prod'
ALLOWED_HOSTS='.localhost','.herokuapp.com','.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```
## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=os.config('SECRET_KEY')
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [Pipenv](https://github.com/pypa/pipenv) - Dependency Management

## Versioning

We use [Git](https://git-scm.com/) for versioning. 

## Codebeat Grade
[![codebeat badge](https://codebeat.co/badges/044785d4-b2fc-4d8f-a084-2b38e627b2aa)](https://codebeat.co/projects/github-com-d0nmoses-dagram-master)


## Authors

* *Don Moses** - *Initial work* 

## License
[LICENSE](License)

## Acknowledgments

* Lawrence Karanja
* Ashley Zawadi
