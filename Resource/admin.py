from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Resource)
admin.site.register(Book)
admin.site.register(Document)
admin.site.register(Publication)
admin.site.register(WebLink)