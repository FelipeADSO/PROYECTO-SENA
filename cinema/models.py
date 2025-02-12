from django.db import models

# Create your models here.

class estrenos (models.Model): 
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    precio = models. DecimalField(max_digits=10, decimal_places=2) 
    stock = models. IntegerField(default=0) 
    imagen = models. ImageField(upload_to='estrenos/', null=True, blank=True)
    
    def str (self): 
        return self.nombre