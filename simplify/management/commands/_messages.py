URLS_CONTENT = """from django.urls import path
from . import views

app_name = "{0}"

urlpatterns = [
    path('', view=views.Index.as_view(), name='index'),
    path('<int:pk>/', view=views.Detail.as_view(), name='detail'),
    path('<int:pk>/', view=views.Edit.as_view(), name='edit'),
    path('create/', view=views.Create.as_view(), name='create'),
]"""

VIEWS_CONTENT = """from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, ListView, DetailView
from django.views.generic.base import TemplateView


# /{0}/
class Index(TemplateView):
    template_name = "{0}/index.html"


# /{0}/create/
class Create(TemplateView):
    template_name = "{0}/create.html"


# /{0}/<:id>/edit/
class Edit(TemplateView):
    template_name = "{0}/edit.html"
    model = "_MY_MODEL_HERE_"


# /{0}/<:id>/
class Detail(DetailView):
    template_name = "{0}/detail.html"
    model = "_MY_MODEL_HERE_"
    paginate_by = 25

"""
