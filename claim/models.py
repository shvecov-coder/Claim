from django.db import models

# Create your models here.

class Claim(models.Model):
    type_claim = models.CharField(max_length=1024)
    select_claim = models.CharField(max_length=1024)
    name_claim = models.CharField(max_length=1024)
    parent_claim = models.CharField(max_length=1024)
    class_claim = models.IntegerField()
    concert_claim = models.CharField(max_length=1024)
    sity_claim = models.CharField(max_length=1024)
    prog_claim = models.TextField()
    url_claim = models.URLField()