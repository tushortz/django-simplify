from django.core.management.base import BaseCommand, CommandError
import os
from simplify.management import _helper
import re
from django.conf import settings


class Command(BaseCommand):
    help = '''Creates a model using the parameters supplied. \nusage: python manage.py create_model <app_name> <model_name> [fields:data_type, ]'''

    def add_arguments(self, parser):
        parser.add_argument('params', nargs='+', type=str)
        

    def handle(self, *args, **options):
        params = options['params']
        module_path = os.environ['DJANGO_SETTINGS_MODULE']

        if len(params) < 3:
            self.stdout.write(self.style.WARNING('python manage.py create_model <app_name> <model_name> [fields:data_type, ]'))
            return

        
        app_name, model_name, *model_fields = params

        _model_template = f"class {model_name}(TimeBasedModel):\n"
        _field_template = ""
        _to_string = "\n    def __str__(self):\n        return self.{}\n"
        model_path = f"{app_name}/models.py"

        if os.path.exists(model_path):
            mode = "r"
        else:
            mode = "w"
            self.stdout.write(self.style.WARNING(f'app "{app_name}" does not exist'))
            return

        # used to check if date/datetime is present to enable import if necessary
        import_timezone = False

        for mf in model_fields:
            field, data_type, *relationship = re.split(r'[:=]', mf)

            if data_type.startswith("date"): import_timezone = True
            if relationship: relationship = relationship[0]
            _field_template += _helper.MODEL_FIELD_TEMPLATE.format(field, _helper.FIELD_MAPPERS[data_type].format(relationship))

        model_code = "\n\n" + _model_template + _field_template + _to_string.format(model_fields[0].split(":")[0])


        with open(model_path, mode) as f:
            content = f.read()

        auto_import = "from simplify.helpers.model_helper import TimeBasedModel\n"
        model_import = "from django.db import models"
        if import_timezone and not auto_import in content:
            auto_import += "from django.utils import timezone\n"

        # prevent import if already present
        if model_import in content and not auto_import in content:
            with open(f"{app_name}/models.py", "w") as f:
                content = content.replace(model_import, auto_import + model_import)
                f.write(content)

        if not _model_template in content:
            with open(f"{app_name}/models.py", "a") as f:
                    f.write(model_code)
                    self.stdout.write(self.style.SUCCESS(f'{app_name}/models.py" updated'))

        # update admin.py      
        with open(f"{app_name}/admin.py") as f:
            content = f.read()

        # dont add to admin if already present
        if re.search(rf".register.*?{model_name}", content):
            self.stdout.write(self.style.WARNING()(f'{app_name}.{model_name} has already been registered'))

            return

        with open(f"{app_name}/admin.py", "w") as f:
            import_ = f"from {app_name}.models import {model_name}\n"
            first_field = model_fields[0].split(":")[0]
            admin_ = f"""
@admin.register({model_name})
class {model_name}Admin(admin.ModelAdmin):
    list_display = ['{first_field}']
    ordering = ['{first_field}']

"""

            
            admin_data = import_ + content + admin_
            f.write(admin_data)
            self.stdout.write(self.style.SUCCESS(f'{app_name}/admin.py" updated'))
