URLS_CONTENT = """from django.urls import path
from . import views

app_name = "{0}"

urlpatterns = [
{1}
]"""

IMPORTS = """from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User

"""


_create = """ 
# /{0}/add
class {1}Create(CreateView):
    template_name = "{0}/create.html"
    model = "_MY_MODEL_HERE_"
    fields = '__all__'
"""

_read = """
# /{0}/<:id>
class {1}Detail(DetailView):
    template_name = "{0}/detail.html"
    model = "_MY_MODEL_HERE_"
"""

_update = """
# /{0}/<:id>/update
class {1}Update(UpdateView):
    template_name = "{0}/update.html"
    model = "_MY_MODEL_HERE_"
    fields = '__all__'
"""

_delete = """
# /{0}/<:id>/delete
class {1}Delete(DeleteView):
    model = "_MY_MODEL_HERE_"
    success_url = reverse_lazy('{0}:index')
"""

_index = """
# /{0}
class {1}Index(ListView):
    template_name = "{0}/index.html"
    model = User # change this
    paginate_by = 25
"""

_template = """
# /{0}
class {1}Index(TemplateView):
    template_name = "{0}/{2}_{3}.html"
    model = User # change this
    paginate_by = 25
"""

CRUDIL_MAP = {
    "c": _create,
    "r": _read,
    "u": _update,
    "d": _delete,
    "i": _index,
    # '_': _template
}

URL_PATTERN_MAP = {
    'c': "path('create', view=views.Create.as_view(), name='create'),",
    'r': "path('<int:pk>', view=views.Detail.as_view(), name='detail'),",
    'u': "path('<int:pk>/update', view=views.Update.as_view(), name='update'),",
    'd': "path('<int:pk>/delete', view=views.Delete.as_view(), name='delete'),",
    'i': "path('', view=views.Index.as_view(), name='index'),",
    # '_': "path('', view=views.{0}.as_view(), name='index'),",
}

ACTION_MAP = {
    "c": 'Create',
    "r": 'Detail',
    "u": 'Update',
    "d": '',
    "i": 'Index',
}

def generate_view_content(app_name, crudil_string='crudi'):
    crudil = list(crudil_string.replace(" ", ''))
    view_content = ""

    for c in crudil:
        if c in CRUDIL_MAP:
            view_content += CRUDIL_MAP[c].format(app_name) + "\n"
    return IMPORTS + view_content
