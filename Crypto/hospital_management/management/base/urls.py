from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/login', doctor_login, name='doctor_login'),
    path('patient/login', patient_login, name='patient_login'),
    path('doctor/upload', upload_file, name='file_upload'),
    path('patient/list', file_list, name='file_name'),
    path('patient/list/<filename>', download_file, name='download_file'),
    path('doctor/home', doctor_home, name='doctor_home'),
    path('patient/home', patient_home, name='patient_home'),
    path('appointment/', show_appointment, name='appointments'),
    path('appointment/add', add_appointment, name='appointment_add'),
    path('pharmacy/add', pharmacy_add, name='add_pharmacy'),
    path('pharmacy', pharmacy_view, name='view_pharmacy'),
    path('feedback', show_feedback, name='show_feedback'),
    path('feedback/add', add_feedback, name='add_feedback')
]
