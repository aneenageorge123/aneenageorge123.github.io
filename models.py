from django.db import models

# Create your models here.
class admindb(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email     = models.CharField(max_length=20)
    username  = models.CharField(max_length=20)
    password  = models.CharField(max_length=20)
    age       = models.CharField(max_length=20)
    gender    = models.CharField(max_length=20)
    image     = models.ImageField(upload_to='image/',default="")