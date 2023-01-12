from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File_handler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length= 255)
    enctrypted_file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.filename