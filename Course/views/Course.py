from django.core import serializers
from django.http import HttpResponse
from Course.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json

# input : courseId, courseName, courseType, credits, sessMaxMarks, endMaxSemMarks, maxMarks, minPassingMarks, semester, degreeCode, degreeType, branchCode
@csrf_exempt
@require_POST
def addCourse(request):
	C = Course.objects.addCourse(request.POST)
	data = serializers.serialize('json', [ C, ])
	print(data)
	return HttpResponse(data, content_type='application/json')

@csrf_exempt
@require_GET
def retrieveCourses(request):
	C = Course.objects.retrieveCourses(request.GET)
	data = serializers.serialize('json', C)
	return HttpResponse(data, content_type='application/json')
	
@csrf_exempt
@require_GET
def getCourseById(request):
	C = Course.objects.getCourseById(request.GET)
	data = serializers.serialize('json', C)
	return HttpResponse(data, content_type='application/json')
	