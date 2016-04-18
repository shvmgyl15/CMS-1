from django.db import models
from Course.models import Course
from Profiler.models import Faculty
from Resource.models import Book,Document,Publication,WebLink

class ResourceManager(models.Manager):
	def addResource(self,request):
		C = Course.objects.get(request['courseId'])
		F = Faculty.objects.get(request['dtuRegId'])
		'''here type for resource has been named as resourceType as there is another type field
		available in the Book class'''
		R = Resource(
			type = request['resourceType'],
			course = C,
			updated_by = F
		)
		R.save()
		if request['resourceType']==0:
			bookId = {'bookId':R.id}
			request.append(bookId)
			B = Book.objects.addBook(request)
			return R

		if request['resourceType']==1:
			publicationId = {'publicationId':R.id}
			request.append(publicationId)
			B = Book.objects.addBook(request)
			return R

		if request['resourceType']==2:
			documentId = {'documentId':R.id}
			request.append(documentId)
			B = Book.objects.addBook(request)
			return R

		if request['resourceType']==3:
			webLinkId = {'webLinkId':R.id}
			request.append(webLinkId)
			B = Book.objects.addBook(request)
			return R
		
	def retrieveResources(self, request):
		C = Course.objects.getCourseById(request)
		R = Resource.objects.filter(course = C)
		return R
	
	def getResourceById(self, request):
		R = Resource.objects.get(id = request['id'])
		return R

class Resource(models.Model):
	BOOK = 0
	PUBLICATION = 1
	DOCUMENT = 2
	WEBLINK = 3
	RESOURCE_TYPE_CHOICES = (
		(BOOK, 'Book'), (PUBLICATION, 'Publication'), (DOCUMENT, 'Document'), (WEBLINK, 'Web Links') )

	type = models.PositiveIntegerField(choices=RESOURCE_TYPE_CHOICES, blank=False, null=False)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
	updatedOn = models.DateTimeField(auto_now=True)
	updatedBy = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=False)

	def __str__(self):
		return self.type+ "-" +self.updatedOn


addDr = {
	'courseId':'SE202',
	'dtuRegId':'',
	'resourceType':'0',
	'name':'Data Structures',
	'author':'R.S. Pillai',
	'edition':'2',
	'type':'0',
	'publisher':'evergreen'
}
