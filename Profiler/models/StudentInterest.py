from django.db import models
from Profiler.models import *

class StudentInterestManager(models.Manager):
    def addStudentInterestManager(self, request):
        SI = StudentInterest(
            student = Student.objects.get(rollNo = request['rollNo']), 
            interest = Interest.objects.get(tag = request['tag'])
        )
        SI.save()
        return SI
    
    def deleteStudentInterestManager(self, request):
        SI = StudentInterest.objects.get(student = Student.objects.get(rollNo = request['rollNo'])).get(interest = Interest.objects.get(tag = request['tag']))
        SI.delete()
        return SI
        
    def retrieveStudentInterest(self, request):
        S = Student.objects.get(rollNo = request['rollNo'])
        objList = StudentInterest.objects.filter(
            student = S
        )
        return objList

class StudentInterest(models.Model):
    #student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=False)
    #interest
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE, default=False)

    objects = StudentInterestManager()

    def __str__(self):
        return str(self.student + "_" + self.interest)