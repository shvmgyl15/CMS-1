from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^addCourse', views.addCourse, name='addCourse'),
    url(r'^getCourse', views.getCourse, name='getCourse'),
]
