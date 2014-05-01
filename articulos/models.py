from django.db import models

class Autor(models.Model):
	primer_nombre=models.CharField(max_length=30)
	Apellido=models.CharField(max_length=40)
	
	def __unicode__(self):
		return u'%s %s' %(self.primer_nombre, self.Apellido)

class Articulo(models.Model):
	titulo=models.CharField(max_length=100)
	autor=models.ManyToManyField(Autor)
	url=models.URLField()
	descripcion=models.CharField(max_length=500)
	fecha_publicacion=models.DateField()	
	
	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering= ['Apellido']
	

