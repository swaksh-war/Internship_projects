from django.urls import path
from .views import home, user_login, user_register, show_pub_key, upload_and_encrypt, list_of_encrypted_file, decrypt_file, user_logout, upload_and_encrypt_layer2, decrypt_file2, file_list3
urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('publickey/', show_pub_key, name='showpublickey'),
    path('encrypt/', upload_and_encrypt, name='encrypt'),
    path('list/', list_of_encrypted_file, name='fileList'),
    path('list/<filename>', decrypt_file, name='decrypt'),
    path('logout/', user_logout, name='userLogout'),
    path('encryptl3/', upload_and_encrypt_layer2, name='encryptl3'),
    path('list3/', file_list3, name='list3'),
    path('list3/<filename>', decrypt_file2, name='decryptl3')
]
