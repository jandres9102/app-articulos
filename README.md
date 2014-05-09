app-articulos
=============

 Crear una aplicación django para empezar a listar/crear/borrar y actualizar artículos en internet (titulo, autor, url, descripción, fecha de publicación)
Nombre bd=articulos
nombre app=articulos


Las siguientes son  lineas de comando que digite para realizar las diversas operaciones en consola:
crear
from articulos.models import Autor
a1=Autor.objects.create(primer_nombre='Andres', Apellido='Villarraga')

buscar 
Autor.objects.filter(primer_nombre="Andres"
, Apellido=”Villarraga)

listar
lista_autores= Autor.objects.all()


ordenar
Autor.objects.order_by("Apellido)”
Autor.objects.order_by("primer_nombre","Apellido")
Autor.objects.order_by("-primer_nombre","Apellido")
 ordena al reves

Encadenar busquedas:
>>> from articulos.models import Autor
>>> Autor.objects.filter(primer_nombre="Andrea").order_by("-Apellido")

trocear datos
Autor.objects.order_by('Apellido')[0:2] 

Actualizar datos

a=Autor.objects.get(primer_nombre="Andrea",Apellido="Sicacha")
>>> a.Apellido="Rodriguez"
>>> a.save()

Autor.objects.all().update(Apellido=” Amador”)


Eliminar

>>> p=Autor.objects.filter(Apellido="Ortiz").delete()
>>> p=Autor.objects.get(Apellido="Cruz").delete()
>>> Autor.objects.all().delete()

https://github.com/jandres9102/app-articulos.git
