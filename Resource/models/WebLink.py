from django.db import models
#from Resource.models import Resource

class WebLink(models.Model):
    webLinkId = models.ForeignKey('Resource.Resource', on_delete=models.CASCADE, default=False, primary_key=True)
    link = models.URLField(max_length=256, null=False, blank=False)