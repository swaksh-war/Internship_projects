from django.urls import path
from .views import home, user_register, user_login, two_factor_authenticate, user_logout, view_public_key, upload_and_encrypt, list_of_encrypted_file, decrypt_file
urlpatterns = [
    path('', home, name='home'),
    path('register', user_register, name='user_register'),
    path('login', user_login, name='user_login'),
    path('verify', two_factor_authenticate, name='auther'),
    path('logout', user_logout, name='user_logout'),
    path('publickey',view_public_key, name='public_key'),
    path('encrypt/', upload_and_encrypt, name='encrypt'),
    path('list/', list_of_encrypted_file, name='fileList'),
    path('list/<filename>', decrypt_file, name='decrypt'),
]
