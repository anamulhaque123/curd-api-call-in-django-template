from django.db import models

# Create your models here.
class client(models.Model):
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=100)
    priority = models.IntegerField()
    created_by  = models.CharField(max_length=100)