from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=8)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.username

class DailyAccess(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    data = models.DateField(default=now)

    class Meta:
        unique_together = ('username', 'ip_address', 'data')
