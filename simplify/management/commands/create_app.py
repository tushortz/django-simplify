from django.core.management.base import BaseCommand, CommandError
import os
from simplify.management import _messages, _command_functions
import re
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates an app including urls.py'

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='+', type=str)

    def handle(self, *args, **options):
        params = options['app_name']

        if len(params) < 1:
            _command_functions.issue_warning(self)
    

        app_name, *crud_value = params
        if crud_value: 
            crud_value = crud_value[0]
        else:
            crud_value = 'crudi'

        # needs a redirect to index if delete is present
        if "d" in crud_value and "i" not in crud_value:
            crud_value += "i"

        if not os.path.exists(app_name):
            os.system(f"django-admin startapp {app_name}")
        else:
            self.stdout.write(self.style.WARNING(f'"{app_name}" already exists'))

        # this must preceed because it creates the necessary folders
        _command_functions.create_views(self, app_name, crud_value)
        _command_functions.create_templates(self, app_name, crud_value)
        _command_functions.create_urls(self, app_name, crud_value)
        _command_functions.add_app_url_to_urlpatterns(self, app_name)

