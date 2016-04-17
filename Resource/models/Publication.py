from django.db import models
#from Resource.models import Resource

class Publication(models.Model):
    publicationId = models.ForeignKey('Resource.Resource', on_delete=models.CASCADE, default=False, primary_key=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    authors = models.CharField(max_length=70)
    publicationDate = models.DateField(editable=True, auto_now=False, auto_now_add=False)
    organization = models.CharField(max_length=70)
    webLink = models.URLField(max_length=256)