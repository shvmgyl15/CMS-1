from django.core import serializers
from django.http import HttpResponse
from Announcements.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

@csrf_exempt
@require_POST
def addAnnouncement(request):
	A = Announcements.objects.addAnnouncement(request.POST)
	data = serializers.serialize('json', [ A, ])
	return HttpResponse(data, content_type='application/json')

@csrf_exempt
@require_GET
def retrieveAnnouncements(request):
	A = Announcements.objects.retrieveAnnouncements(request.GET)
	data = serializers.serialize('json', A)
	return HttpResponse(data, content_type='application/json')
	
@csrf_exempt
@require_GET
def getAnnouncementById(request):
	A = Announcements.objects.getAnnouncementById(request.GET)
	data = serializers.serialize('json', A)
	return HttpResponse(data, content_type='application/json')
