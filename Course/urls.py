from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^addCourse', views.addCourse, name='addCourse'),
    url(r'^retrieveCourses', views.retrieveCourses, name='retrieveCourses'),
    url(r'^getCourseById', views.getCourseById, name='getCourseById'),
]
