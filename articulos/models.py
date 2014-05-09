from django.db import models

class Author(models.Model):
	name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	
	def __unicode__(self):
		return u'%s %s' %(self.name, self.last_name)

class Article(models.Model):
	title=models.CharField(max_length=100)
	authors=models.ManyToManyField(Author)
	url=models.URLField()
	description=models.CharField(max_length=500)
	save_date=models.DateField()	
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering= ['title']
	
class Account(models.Model):
	user=models.CharField(max_length=10)
	password=password = models.CharField(max_length=16)
	email = models.EmailField()
	articles=models.ForeignKey(Article)

	def __unicode__(self):
		return self.user
