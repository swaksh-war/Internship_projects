from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Appointment_dets(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Feedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class File_handler(models.Model):
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True)
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True)
    filename = models.CharField(max_length=500)
    fernetkey1 = models.CharField(max_length=500)
    fernetkey2 = models.CharField(max_length=500)
    encrypted_file_path = models.CharField(max_length=500)

    def __str__(self):
        return self.filename