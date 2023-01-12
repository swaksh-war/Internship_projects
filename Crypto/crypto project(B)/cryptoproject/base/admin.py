from django.contrib import admin
from .models import file_handler, account, file_handler_three

# Register your models here.
admin.site.register(file_handler)
admin.site.register(account)
admin.site.register(file_handler_three)