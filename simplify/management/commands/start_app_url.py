from django.core.management.base import BaseCommand, CommandError
import os
from simplify.management.commands import _messages
import re
from django.conf import settings
from pprint import pprint


class Command(BaseCommand):
    help = 'Creates an app including urls.py'

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='+', type=str)

    def handle(self, *args, **options):
        app_name = options['app_name']
        module_path = os.environ['DJANGO_SETTINGS_MODULE']

        if len(app_name) < 1:
            self.stdout.write(self.style.WARNING('use command:  python manage.py start_app_url app_name'))
            return

        app_name = app_name[0]
        urls_content = _messages.URLS_CONTENT

        if not os.path.exists(app_name):
            os.system(f"django-admin startapp {app_name}")
        else:
            self.stdout.write(self.style.WARNING(f'"{app_name}" already exists'))

        with open(f"{app_name}/urls.py", "w") as f:
            f.write(urls_content)

        mod_path = module_path.replace(".", "/")
        with open(f"{mod_path}.py") as f:
            content = f.read()

        ia = re.search(r'INSTALLED_APPS = \[(.*?)\]', content, re.MULTILINE | re.DOTALL)

        if ia:
            ia = ia.group(1)
            content = content.strip("\n")
            content = re.sub(r'(,[\s\n],)', '', content)

            content = content.replace(ia, ia.rstrip("\n") + f",\n    '{app_name}',\n")
            
            if not app_name in ia:
                with open(f"{mod_path}.py", "w") as f:
                    f.write(content)

        self.stdout.write(self.style.SUCCESS('Successfully created app with urls.py'))