from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from Profiler.models import Faculty

class NewsManager(models.Manager):
	def addNews(self,request):
		publishedByObj = Faculty.getFacultyByFacultyId(request)

		N = News(
				headline = request['headline'],
				description = request['description'],
				image =  request['image'],
				link = request['url'],
				date = request['date'],
				publishedBy = publishedByObj
			)
		N.save()
		return N

	def getNewsById(self,request):
		"""get news details based on news id"""
		N = News.objects.get(id = request['id'])
		return N

	def retrieveLatestNews(self,request):
		last_ten = News.objects.filter(date = request['since']).order_by('-date')[:10]
		return last_ten
	
	def retrieveMoreNews(self, request):
		N = News.objects.all()
		paginator = Paginator(contact_list, request['rowsPerPage']) 

		page = request['page']
		try:
			news = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			news = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			news = paginator.page(paginator.num_pages)

		return news
	
	def getDetailsById(request):
		N = News.objects.get(request['id'])
		return N
	
	def deleteNews(self, request):
		"""deletes news"""
		N = News.objects.get(request['id'])
		N = N.delete()
		return N
	
	def editNews(self, request):
		pass


class News(models.Model):
	#Headline
	headline = models.CharField(max_length=100,null=False,blank=False)
	#Desciption
	description = models.CharField(max_length=4000,null=False,blank=False)
	#Image
	image = models.URLField(null=True, blank=True)
	#Link
	link = models.URLField(null=True, blank=True)
	#Date
	date = models.DateField(auto_now=False, auto_now_add=True)
	#Published By
	publishedBy = models.CharField(max_length=100,null=False,blank=False)

	objects = NewsManager()

	def __str__(self):
		return self.headline
