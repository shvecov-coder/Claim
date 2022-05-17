from django.db import models

# Create your models here.

class Claim(models.Model):
    type_claim = models.IntegerField() # формат
    select_claim = models.IntegerField() # номинация
    name_claim = models.CharField(max_length=1024) # фио участника/название коллектива
    parent_claim = models.CharField(max_length=1024) # преподаватель
    class_claim = models.IntegerField()
    concert_claim = models.CharField(max_length=1024)
    sity_claim = models.CharField(max_length=1024)
    prog_claim = models.TextField()
    url_claim = models.URLField()