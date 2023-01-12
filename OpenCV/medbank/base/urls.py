from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('donorregister', register_donor, name='register_donor'),
    path('ngoregister', register_ngo, name='register_ngo'),
    path('donorlogin', login_donor, name='login_donor'),
    path('ngologin', login_ngo, name='login_ngo'),
    path('logout', custom_logout, name = 'logout'),
    path('uploadmed', upload_med, name = 'upload_med'),
    path('viewmed', view_med, name='view_med'),
    path('search/', search_query, name='search'),
    path('aboutus', about_us, name='about_us')
]
