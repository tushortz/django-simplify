# Django Simplify


## Introduction

Django simplify provides Ruby on Rails-like command line functionalities, models and helper functions so you can focus on development and removes the pain of repeating frequent actions.

## Requirements

* Python `3.6` and above
* Django (tested with 3.1, probably works with any version that supports
  Python 3)

## Installation

`django-simplify` can be installed via pip.


```sh
$ pip install django-simplify
```

Then just add `simplify` to your `INSTALLED_APPS`.


Below are several example commands you can run

You can run the demo project using the following commands:

```sh
$ python manage.py create_app <app_name>
```

## Features

- TimeBasedModel (gives you access to `created_at` and `updated_at` field)
- NamedTimeBasedModel - gives you access to the fields `name`, `created_at` and `updated_at`
- automatically create a urls.py file
- adds newly created app in the installed apps when you run the `python manage.py create_app <app_name>` command
- creates `index`, `edit`, `create` and `detail` view + templates
- updates the `project.urls` with the latest `app`


You can import the helper models above and inherit from them. See example

**models.py**

```python
from simplify.helpers.model_helper import TimeBasedModel, NamedTimeBasedModel

class MyModel(TimeBasedModel):
    extra_fields = ....
```

## Todo
- create model from commandline
- add helper methods
- add documentation
