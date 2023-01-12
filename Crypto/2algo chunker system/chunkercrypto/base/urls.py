from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('encrypt/', upload_and_encrypt, name='encrypt'),
    path('list/', list_of_encrypted_file, name='fileList'),
    path('list/<filename>', decrypt_file, name='decrypt'),
    path('login/', userlogin, name='login'),
    path('register/', userregister, name='register'),
    path('logout/', userlogout, name='logout')
]

