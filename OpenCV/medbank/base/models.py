from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your models here.

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    exp_date = models.DateTimeField(blank=False)
    image = models.FileField(upload_to='med_image')
    category = models.CharField(max_length=50, default='unknown')

    def __str__(self):
        return self.name

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gov_recognition = models.CharField(max_length=5, default='No')
    contact = models.IntegerField()
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
