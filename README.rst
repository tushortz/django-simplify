=========================================
Django Simplify
=========================================


Introduction
=========================================


Django simplify provides Ruby on Rails-like command line functionalities, models and helper functions so you can focus on development and removes the pain of repeating frequent actions.

Requirements
--------------

* Python `3.6` and above
* Django (tested with 3.1, probably works with any version that supports
    Python 3)

Installation
---------------

**django-simplify** can be installed via pip.


.. code-block:: bash

    $ pip install django-simplify

    
Then just add `simplify` to your `INSTALLED_APPS`.


Below are several example commands you can run.

.. code-block:: bash

    $ python manage.py create_app <app_name>


Features
-----------

* timestamp for every model
* alphabetic filter for admin
* model, view, template and url route generator
* automatic import


Helper models
################

- simplify.helpers.model_helper.TimeBasedModel
    - Provides the `created_at` and `updated_at` fields for timestamp

- simplify.helpers.model_helper.NamedTimeBasedModel
    - Provides the `name`, `created_at` and `updated_at` fields.
  
- simplify.helpers.admin_helper.AlphaNumericFilterAdmin
    - when subclassed, it allows the items to be filtered alphabetically by either A-Z or 0-9
    - **Note**: for this to work, you must specify values for `alphanumeric_filter` in the model admin.


Usage
######

.. code-block:: python

  # models.py
  from simplify.helpers.model_helper import TimeBasedModel, NamedTimeBasedModel
  
  class MyModel(TimeBasedModel):
      extra_fields = ....



.. code-block:: python

  # admin.py
  from simplify.helpers.admin_helper import AlphaNumericFilterAdmin
  
  class MemberAdmin(AlphaNumericFilterAdmin):
      alphanumeric_filter = ["first_name", "last_name", 'age'] # this part is what creates the filter
      list_filter = ['age']
      list_display = ['first_name', 'last_name',]


Management commands
#########################

**1. create_app**

- automatically adds a `urls.py` file after app is created.
- adds newly created app in the settings.py file under `INSTALLED_APPS`
- creates `index`, `edit`, `create` and `detail` view and respective templates
- adds the app route to your project's `urls.py` file
    

Usage
###########

.. code-block:: bash

    $ python manage.py create_app <app_name>


**2. create_model**

Creates a model and their respective fields. the following types maps to respective Django model fields. It will also add the app to the django admin too.


- 121, o2o or set -> OneToOneField
- bool -> BooleanField
- date -> DateField
- datetime or dt -> DateTimeField
- dict or m2m -> ManyToManyField
- email -> EmailField
- file -> FileField
- list or fk -> ForeignKey
- float -> FloatField
- dec -> DecimalField
- img or image -> ImageField
- int -> IntegerField
- str or char -> CharField
- txt or text -> TextField
    

Usage
########

.. code-block:: bash

    $ python manage.py create_app <app_name> <model_name> field_name:type field_name:type ... 


an example
###########

.. code-block:: bash

    $ python manage.py create_app member Member first_name:text last_name:text age:int


will generate the following code in the `member/models.py` file

.. code-block:: python

    class Member(TimeBasedModel):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        age = models.IntegerField(default=0)

        def __str__(self):
            return self.first_name


.. note:: The command uses the first specified field as the `__str__` default.


Specifying relationships
###########################

Specifying `ForeignKey`, `OneToOneField` or `ManyToManyField` is quite easy. just add an `=<related_model>`. See example

.. code-block:: bash

    $ python manage.py create_app <app_name> <model_name> field_name:type=related_model

    # an example
    # if the related model is in the same models.py file, specify it as app_name.Model
    $ python manage.py create_app author Author name:char books:fk=Book # or   
    $ python manage.py create_app author Author name:char books:fk=author.Book 

    # if in a different app. (say book model)
    # obviously you should be able to substitute fk with m2m, o2o, 121
    $ python manage.py create_app author Author name:char books:fk=book.Book 


will create the following

.. code-block:: bash

    class Author(TimeBasedModel):
        name = models.CharField(max_length=50)
        books = models.ForeignKey('book.Book', on_delete=models.CASCADE)

        def __str__(self):
            return self.name



**3. create_view**

Creates a view, generate its respective template and adds the path in the urls.py file

Usage
########

.. code-block:: bash

    $ python manage.py create_view <app_name> <view_name> 


an example
###########

.. code-block:: bash

    $ python manage.py create_view member MemberDetail


    
Todo
-----

- add more helper functions
- add documentation


.. note:: 

    This is still in early development mode. might have bugs. It works fine if you write good code and follow the django style of development. Please fork the project to make contributions
