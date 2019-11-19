from django.db import models
from django.utils import timezone

class AnimeM(models.Model):
    nombre              = models.CharField(max_length=30)
    id_anime         = models.AutoField(primary_key=True)
    image_anime      = models.ImageField(blank=True,null=True,upload_to = "anime/%Y/%m/$d/")      
    descripcion         = models.CharField(max_length=300)
 
    def __str__(self):
        return self.nombre

