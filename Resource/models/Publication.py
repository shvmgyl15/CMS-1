from django.db import models


class Publication(models.Model):
    publicationId = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=150, blank=False, null=False)
    authors = models.CharField(max_length=70)
    publicationDate = models.DateField(editable=True, auto_now=False, auto_now_add=False)
    organization = models.CharField(max_length=70)
    webLink = models.URLField(max_length=256)