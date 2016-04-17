from django.db import models
#from Resource.models import Resource

class Document(models.Model):
    WORD_DOCUMENT = 0
    TEXT_FILE = 1
    PRESENTATION = 2
    PDF = 3
    DOCUMENT_TYPE_CHOICES = (
        (WORD_DOCUMENT, 'Word Document'), (TEXT_FILE, 'Text File'), (PRESENTATION, 'Presentation'), (PDF, 'PDF') )

    documentId = models.ForeignKey('Resource.Resource', on_delete=models.CASCADE, default=False, primary_key=True)
    type = models.PositiveIntegerField(choices=DOCUMENT_TYPE_CHOICES, blank=False, null=False)
    source = models.URLField(max_length=256, null=False, blank=False)