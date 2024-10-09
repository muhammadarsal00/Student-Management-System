from django.db import models

# Create your models here.
from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=128)

