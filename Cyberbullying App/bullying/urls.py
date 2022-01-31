from django.urls import path
from django.urls import re_path
from . import views

app_name = 'bullying'

urlpatterns = [
    re_path(r'^$', views.choose_bullying, name="choose_bullying"),
]
