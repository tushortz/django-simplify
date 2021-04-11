from django.core.management.base import BaseCommand, CommandError
import os
from simplify.management import _messages
import re
from django.conf import settings


class Command(BaseCommand):
    help = 'Creates an app including urls.py'

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='+', type=str)

    def handle(self, *args, **options):
        app_name = options['app_name']
        module_path = os.environ['DJANGO_SETTINGS_MODULE']

        if len(app_name) < 1:
            self.stdout.write(self.style.WARNING('use command:  python manage.py create_app <app_name>'))
            return

        app_name = app_name[0]
        urls_content = _messages.URLS_CONTENT.format(app_name)

        # create and populate urls
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

            if not app_name in settings.INSTALLED_APPS:
                with open(f"{mod_path}.py", "w") as f:
                    f.write(content.replace(",,", ","))

        self.stdout.write(self.style.SUCCESS(f'Successfully created\n-- app "{app_name}"\n-- {app_name}/urls.py'))

        # create templates
        path = f"{app_name}/templates/{app_name}"
        actions = ["Index", "Detail", "Edit", "Create"]

        os.makedirs(path, exist_ok=True)
        for action in actions:
            html_file_path = f"{path}/{action.lower()}.html"

            if not os.path.exists(html_file_path):
                with open(html_file_path, "w") as f:
                    f.write(f"<h1>{action.title()}</h1>")
            
            self.stdout.write(self.style.SUCCESS(f'-- {html_file_path}'))

        # create views
        with open(f"{app_name}/views.py", "w") as f:
            f.write(_messages.VIEWS_CONTENT.format(app_name))
            self.stdout.write(self.style.SUCCESS(f'-- {app_name}/views.py'))


        # update project urls
        project_url_path = f'{settings.ROOT_URLCONF.replace(".", "/")}.py'

        with open(project_url_path) as f:
            _content = f.read()
            
        if not f"{app_name}.urls" in _content:
            with open(project_url_path, "w") as f:
                if not re.match(r'from django.urls .*?include', _content):
                    _content = _content.replace("from django.urls import path", 
                                "from django.urls import path, include")
                
                _content = _content.replace("urlpatterns = [", 
                    f"urlpatterns = [\n    path('{app_name}/', include('{app_name}.urls', namespace='{app_name}')),")
                f.write(_content)
                self.stdout.write(self.style.SUCCESS(f'-- {app_name}/urls.py updated'))

