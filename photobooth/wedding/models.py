from django.db import models

# Create your models here.

class Collage(models.Model):
    collage_name = models.CharField(max_length=50)

class Picture(models.Model):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE)
    picture_name = models.CharField(max_length=50)
    picture_url = models.CharField(max_length=200)
