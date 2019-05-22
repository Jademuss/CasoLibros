from django.db import models
from django.utils import timezone

class ProductosM(models.Model):
    nombre              = models.CharField(max_length=30)
    id_producto         = models.AutoField(primary_key=True)
    image_producto      = models.ImageField(blank=True,null=True,upload_to = "producto/%Y/%m/$d/")
    precio              = models.PositiveIntegerField()   
    descripcion         = models.CharField(max_length=500)
 
    def __str__(self):
        return self.nombre

