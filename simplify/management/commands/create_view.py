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

        if len(params) != 2:
            self.stdout.write(self.style.WARNING("Use format python manage.py create_view <app_name> <view_name> <view_action e.g. c,r,u,d, or i>"))
    

        app_name, view_name, *crud_value = params
        if crud_value: 
            crud_value = crud_value[0][0]
        else:
            crud_value = 'l'
        

        view_snakify = re.sub(r'(?<!^)(?=[A-Z])', '_', view_name).lower()

        # create views
        with open(f"{app_name}/views.py", "a") as f:

            view_content = f'''
class {view_name}View(TemplateView):
    template_name = "{app_name}/{view_snakify}.html"
'''            
            f.write(view_content)
            self.stdout.write(self.style.SUCCESS(f'-- {app_name}/views.py updated'))


        path = f"{app_name}/templates/{app_name}"
        html_file_path = f"{path}/{view_snakify}.html"
        
        if not os.path.exists(html_file_path):
            with open(html_file_path, "w") as f:
                f.write(f"<h1>{app_name.title()} {view_name.title()}</h1>")
                self.stdout.write(self.style.SUCCESS(f'-- {html_file_path} created'))

        
        with open(f"{app_name}/urls.py") as f:
            content = f.read()
            view_opts = view_snakify.replace("_", "-")
            content = re.sub(r'(urlpatterns = \[)', "urlpatterns = [\n    "
                    + f"""path('{view_opts}', view=views.{view_name}View.as_view(), name='{view_opts}'),""", content)

        with open(f"{app_name}/urls.py", "w") as f:
            f.write(content)
