from django.db import models

class InterestManager(models.Manager):
    def addInterest(self, request):
        I = Interest(
            tag = request['tag']
        )
        I.save()
        return I
        
    def editInterest(self, request):
        I = Interest.objects.get(tag = request['tag'])
        I.save()
        return I
        
    def deleteInterest(self, request):
        I = Interest.objects.get(tag = request['tag'])
        I.delete()
        return I
        
    def retrieveInterests(self, request):
        objList = Interest.objects.all();
        return objList

class Interest(models.Model):
    #tag
    tag = models.SlugField(max_length=50)
    
    objects = InterestManager()
    
    def __str__(self):
        return str(self.tag)