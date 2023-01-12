from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_key = models.UUIDField()

    def __str__(self):
        return self.user.username

class FileHandler(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    filename = models.CharField(max_length = 200)
    encrypted_file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.filename

