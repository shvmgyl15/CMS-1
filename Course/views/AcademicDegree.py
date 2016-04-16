from django.core import serializers
from django.http import HttpResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

@csrf_exempt
@require_GET
def retrieveDegrees(request):
	C = Degree.objects.retrieveDegrees(request.GET)
	data = serializers.serialize('json', C)
	return HttpResponse(data, content_type='application/json')

	
@csrf_exempt
@require_GET
def getDegreeByCodeAndType(request):
	C = Degree.objects.getCourseById(request.GET)
	data = serializers.serialize('json', C)
	return HttpResponse(data, content_type='application/json')
	