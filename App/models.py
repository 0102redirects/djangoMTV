from django.db import models

# Create your models here.

class UserModel(models.Model):
    u_name = models.CharField(max_length=16)
    u_password = models.CharField(max_length=128)

    u_icon = models.ImageField(upload_to='icons')
