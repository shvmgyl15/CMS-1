from django.db import models
from Profiler.models import *

class FacultyInterestManager(models.Manager):
    def addFacultyInterestManager(self, request):
        FI = FacultyInterest(
            Faculty = Faculty.objects.get(rollNo = request['rollNo']),
            interest = Interest.objects.get(tag = request['tag'])
        )
        FI.save()
        return FI
    
    def deleteFacultyInterestManager(self, request):
        FI = FacultyInterest.objects.get(
            Faculty = Faculty.objects.get(rollNo = request['rollNo'])).get(
            interest = Interest.objects.get(tag = request['tag'])
        )
        FI.delete()
        return FI
        
    def retrieveFacultyInterest(self, request):
        F = Faculty.objects.get(rollNo = request['rollNo'])
        objList = FacultyInterest.objects.filter(
            Faculty = F
        )
        return objList

class FacultyInterest(models.Model):
    #faculty
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=False)
    #interest
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE, default=False)

    objects = FacultyInterestManager()
    
    def __str__(self):
        return str(self.Faculty + "_" + self.interest)