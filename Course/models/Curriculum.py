from django.db import models
from Profiler.models import Student
from Course.models import *

class CirriculumManager(models.Manager):
    def retrieveCirriculum(self, request):
        C = Course.objects.get(courseId = request['courseId'])
        objlist  = Cirriculum.objects.filter(course = C)
        return objlist 

class Cirriculum(models.Model):
    #Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = False)
    #Unit
    unit = models.PositiveIntegerField()
    #description
    description = models.TextField()
    
    objects = CirriculumManager()
    
    def __str__(self):
        return str(self.course)
    