from django.contrib import admin
from .models import Patient, Doctor, File_handler, Appointment_dets, Feedback, Pharmacy

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(File_handler)
admin.site.register(Appointment_dets)
admin.site.register(Feedback)
admin.site.register(Pharmacy)

# Register your models here.
