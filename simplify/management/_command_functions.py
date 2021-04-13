from django.conf import settings
import re
from simplify.management import _messages
import os


def add_app_url_to_urlpatterns(command, app_name):
    # update project urls
    project_url_path = f'{settings.ROOT_URLCONF.replace(".", "/")}.py'
    
    with open(project_url_path) as f:
        _content = f.read()
        
    if not f"{app_name}.urls" in _content:
        with open(project_url_path, "w") as f:
            if not re.search(r'import.*?include', _content):
                _content = _content.replace("from django.urls import path", 
                            "from django.urls import path, include")
            
            
            _content = _content.replace("urlpatterns = [", 
                f"urlpatterns = [\n    path('{app_name}/', include('{app_name}.urls', namespace='{app_name}')),")
            f.write(_content)
            command.stdout.write(command.style.SUCCESS(f'-- {app_name}/urls.py updated'))



def create_views(command, app_name, crud_value):
    # create views
    with open(f"{app_name}/views.py", "w") as f:
        view_content = _messages.generate_view_content(app_name, crud_value)
        f.write(view_content)
        command.stdout.write(command.style.SUCCESS(f'-- {app_name}/views.py'))


def create_templates(command, app_name, crud_value):
    # create templates
    path = f"{app_name}/templates/{app_name}"

    os.makedirs(path, exist_ok=True)
    for c in crud_value:
        action = _messages.ACTION_MAP.get(c)
        
        if action:
            html_file_path = f"{path}/{action.lower()}.html"
            
            if not os.path.exists(html_file_path):
                with open(html_file_path, "w") as f:
                    f.write(f"<h1>{app_name.title()} {action.title()}</h1>")
                    command.stdout.write(command.style.SUCCESS(f'-- {html_file_path} created'))


def create_urls(command, app_name, crud_value):
    # create and populate urls
    url_string = ""
    for c in crud_value:
        url = _messages.URL_PATTERN_MAP.get(c)
        
        if url:
            url_string += f"    {url}\n"

    urls_content = _messages.URLS_CONTENT.format(app_name, url_string)

    with open(f"{app_name}/urls.py", "w") as f:
        f.write(urls_content)

    mod_path =  os.environ['DJANGO_SETTINGS_MODULE'].replace(".", "/")
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
                command.stdout.write(command.style.SUCCESS(f'"{app_name}" added to INSTALLED_APPS'))
    command.stdout.write(command.style.SUCCESS(f'Successfully created\n-- app "{app_name}"\n-- {app_name}/urls.py'))


def issue_warning(command):
    command.stdout.write(command.style.WARNING('''
use command:  python manage.py create_app <app_name> [optional:crudi_option].
Where 
    c -> create
    r -> read
    u -> update
    d -> delete
    i -> index

Will creates the five views by default if not specified
'''))
