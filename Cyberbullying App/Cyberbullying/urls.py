from django.urls import path
from django.urls import re_path
from . import views

app_name = 'Cyberbullying'

urlpatterns = [
    re_path(r'^$', views.Cyberbullying_analysis, name="Cyberbullying_analysis"),
    re_path(r'^type/$', views.Cyberbullying_analysis_type, name="Cyberbullying_analysis_type"),
    re_path(r'^import/$', views.Cyberbullying_analysis_import, name="Cyberbullying_analysis_import"),
]
