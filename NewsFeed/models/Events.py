from django.db import models
from Course.models import *
from Profiler.models import Mobile

#just for checking
import datetime

# Manager class for the mobile class
'''class MobileManager(models.Manager):
    def addContacts(self, request):
        """add contact numbers in the database"""
        M = Mobile(
            countryCode=request['countryCode'],
            mobileNum=request['mobileNum']
        )
        M.save()
        return M


#This class is just used to store the mobile number for the required event
class Mobile(models.Model):
    # Country Code
    countryCode = models.PositiveIntegerField(blank=False, null=False)
    # Mobile Number
    mobileNum = models.PositiveIntegerField(blank=False, null=False)

    objects = MobileManager()

    def __str__(self):
        return str(self.countryCode) + "-" + str(self.mobileNum)'''


class EventsManager(models.Manager):
    def addEvent(self, request):
        M = Mobile.objects.addContacts(request)
        E = Events(
            eventName = request['eventName'],
            startDateAndTime = request['startDateAndTime'],
            endDateAndTime = request['endDateAndTime'],
            description = request['description'],
            organisedBy = request['organisedBy'],
            personalMobile = M[0],
            alternativeMobile = M[1],
            email = request['email'],
            fbEvent = request['fbEvent'],
            website = request['website'],
            image = request['image']
        )
        E.save()
        return E

    def editEvent(self,request):
        '''This function will edit the even info by it self and by calling the
        editContact function in MobileManager class'''
        E = Events.objects.get(id = request['id'])
        E.eventName = request['eventName']
        E.startDateAndTime = request['startDateAndTime']
        E.endDateAndTime = request['endDateAndTime']
        E.description = request['description']
        E.organisedBy = request['organisedBy']
        '''contactObjs is only used because editContacts function is returning a list
        of objects'''
        contactObjs = Mobile.objects.editContacts(request)
        E.email = request['email']
        E.fbEvent = request['fbEvent']
        E.website = request['website']
        E.image = request['image']

        E.save()
        return E

    def deleteEvent(self,request):
        E = Events.objects.get(id = request['id'])
        E = E.delete()
        return E


class Events(models.Model):
    #Name of the particular event
    eventName = models.CharField(max_length=50, blank=False, null=False)
    #Start date and time of the event
    startDateAndTime = models.DateTimeField(default=False)
    #End date and time of the event
    endDateAndTime = models.DateTimeField(default=False)
    #Description of the event
    description = models.CharField(max_length=500, blank=False, null=False)
    #Organised By
    organisedBy = models.CharField(max_length=150, blank=False, null=False)
    #Contact Number
    personalMobile = models.ForeignKey(Mobile, related_name="%(class)s_personal_mobile", on_delete=models.CASCADE, default=False)
    alternativeMobile = models.ForeignKey(Mobile, related_name="%(class)s_alternative_mobile", on_delete=models.CASCADE, default=False)
    #email ID
    email = models.EmailField(blank=False, null=False, default=False)
    #Facebook Event Link
    fbEvent = models.CharField(max_length=500, blank=False, null=False)
    #Website
    website = models.CharField(max_length=75, blank=False, null=False)
    #Image
    image = models.URLField(max_length=256, null=True)

    objects = EventsManager()

    def __str__(self):
        return str(self.eventName) + "-" + str(self.startDateAndTime)


mobile0 = {
	'personalMobile':{'countryCode':91,'mobileNum':9999955533},
	'alternativeMobile':{'countryCode':91,'mobileNum':9999955533},
}
drAdd={
    'eventName':'Mid Sems 16',
    'startDateAndTime':'2016-04-04 20:04:50.308998',
    'endDateAndTime':'2016-04-04 20:04:50.308998',
    'description':'Mid Sems Starting 2016',
    'organisedBy':'DTU',
    'personalMobile':{'countryCode':21,'mobileNum':9999955533},
	'alternativeMobile':{'countryCode':21,'mobileNum':9999955533},
    'email':'example@example.com',
    'fbEvent':'www.facebook.com',
    'website':'www.dtu.ac.in',
    'image':'drive.google.co.in/image1'
}

drEditEvent={
    'id':'1',
    'perMobId':'11',
    'altMobId':'12',
    'eventName':'Mid Sems 2016',
    'startDateAndTime':'2016-04-14 20:04:50.308998',
    'endDateAndTime':'2016-04-24 20:04:50.308998',
    'description':'Mid Semesters  2016 are starting',
    'organisedBy':'DTU',
    'personalMobile':{'countryCode':21,'mobileNum':9999955567},
	'alternativeMobile':{'countryCode':21,'mobileNum':9999955598},
    'email':'example@example.com',
    'fbEvent':'www.facebook.com/myEvent',
    'website':'www.dtu.ac.in',
    'image':'drive.google.co.in/image2'
}