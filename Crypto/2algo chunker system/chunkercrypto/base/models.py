from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File_Handler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    encrypted_file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.filename

