from django.contrib import admin
from .models import Medicine, Donor, Ngo

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Donor)
admin.site.register(Ngo)