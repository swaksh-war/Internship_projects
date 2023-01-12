from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

class file_handler(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    filename = models.CharField(max_length=500)
    fernetkeyl1 = models.CharField(max_length=500)
    fernetkeyl2 = models.CharField(max_length=500)
    encrypted_file_path = models.CharField(max_length=500)

    def __str__(self):
        return self.filename

class file_handler_three(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    filename = models.CharField(max_length=500)
    fernetkeyl1 = models.CharField(max_length= 500)
    fernetkeyl2 = models.CharField(max_length=500)
    fernetkeyl3 = models.CharField(max_length=500)
    encrypted_file_path = models.CharField(max_length=500)

    def __str__(self):
        return self.filename

