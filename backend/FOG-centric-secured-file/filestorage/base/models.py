from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FileHandler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads')
    filename = models.CharField(max_length=255)