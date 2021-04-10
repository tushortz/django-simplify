==============================================================================
Django Simplify
==============================================================================

.. .. Travis status:
   
..    .. image:: https://travis-ci.org/WoLpH/django-simplify.svg?branch=master
..      :target: https://travis-ci.org/WoLpH/django-simplify

Introduction
==============================================================================

django simplify allows you focus on development and removes the pain of repeating frequent actions like creating a urls.py. It provides several commands and custom models to make development easier. Attempts to use ruby on rails style commands as well as automate boring processes

Requirements
==============================================================================

* Python `3.6` and above
* Django (tested with 3.1, probably works with any version that supports
  Python 3)

Installation
==============================================================================

`django-simplify` can be installed via pip.


.. code-block:: bash

    pip install django-simplify

Then just add `django-simplify` to your `INSTALLED_APPS`.


Below are several example commands you can run

You can run the demo project using the following commands:

.. code-block:: bash

    python manage.py create_app <app_name>


Features
==============================================================================

- TimeBasedModel (gives you access to `created_at` and `updated_at` field)
- NamedTimeBasedModel - gives you access to the fields `name`, `created_at` and `updated_at`

You can import them using the following command

.. code-block:: python

    from simplify.helpers.model_helper import TimeBasedModel, NamedTimeBasedModel


    class MyModel(TimeBasedModel):
        extra_fields = ....
