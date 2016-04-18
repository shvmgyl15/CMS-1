from django.db import models

class SkillManager(models.Manager):
    def addSkill(self, request):
        S = Skill(
            tag = request['tag']
        )
        S.save()
        return S
        
    def editSkill(self, request):
        S = Skill.objects.get(tag = request['tag'])
        S.save()
        return S
        
    def deleteInterest(self, request):
        S = Skill.objects.get(tag = request['tag'])
        S.delete()
        return S
        
    def retrieveInterests(self, request):
        objList = Skill.objects.all();
        return objList

class Skill(models.Model):
    #tag
    tag = models.SlugField(max_length=50)
    
    objects = SkillManager()
    
    def __str__(self):
        return str(self.tag)