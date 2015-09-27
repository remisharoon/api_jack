from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    job = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()