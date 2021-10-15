from django.db import models
#from django.utils.html import format_html

# Create your models here.


class Paises(models.Model):
    # Id=models.IntegerField().auto_creation_counter
    Abrevation = models.CharField(max_length=2)
    Nombre = models.CharField(max_length=50)
    

    def __str__(self):
        pais = self.Nombre
    
        return pais


class Equipos(models.Model):
    # Id=models.IntegerField().auto_creation_counter
    Nombre = models.CharField(max_length=20)

    def __str__(self):
        equipo = self.Nombre
        return equipo

class Carreras(models.Model):
    # Id=models.IntegerField().auto_creation_counter
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        carrera = self.Nombre
        return carrera

class Modalidad(models.Model):
    # Id=models.IntegerField().auto_creation_counter
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        modalidad = self.Nombre
        return modalidad        

class Botes(models.Model):
    # Id=models.IntegerField().auto_creation_counter No hace falta se crea automaticamente
    Equipo = models.ForeignKey(
        Equipos, null=False, blank=False, on_delete=models.CASCADE)
    Pais = models.ForeignKey(
        Paises, null=False, blank=False, on_delete=models.CASCADE)
    Carrera = models.ForeignKey(
        Carreras, null=True, blank=True, on_delete=models.CASCADE)
    Agno = models.CharField(max_length=4, blank=True, null=True,verbose_name="Año")
    Modalidad = models.ForeignKey(
        Modalidad, null=True, blank=True, on_delete=models.CASCADE)
    PrecioVenta = models.IntegerField(blank=True, null=True)
    CompradoA = models.CharField(max_length=50, blank=True, null=True)
    FechaCompra = models.DateField(blank=True, null=True)
    Observaciones = models.CharField(max_length=200, blank=True, null=True)
    FotoPrincipal=models.ImageField(upload_to=None, blank=True, null=True, verbose_name='FotoPrincipal')

    # Slide=models.

    def __str__(self):
        #bote = str(self.id)+" Carrera:"+str(self.Carrera)+" Equipo:"+str(self.Equipo) + \
        #    " Pais:"+str(self.Pais)+" Año:"+str(self.Agno)
        bote = str(self.id)+":"+str(self.Carrera)+"\n:"+str(self.Equipo) + \
            ":"+str(self.Pais)+":"+str(self.Agno)
        #bote=bote+" Fotos:"+models.Fotos.bote+models.Fotos.Url
        return bote


def get_image_filename(instance, filename):
    idgif = instance.bote.id
    return "DirectorioFotos/%s" % (idgif)


class Fotos(models.Model):
    bote = models.ForeignKey(Botes, null=True, blank=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True, verbose_name='Imagen')

    def __str__(self):
        return str(self.id)+" Foto de: " + str(self.bote)+"\n imagen: "+str(self.imagen)
