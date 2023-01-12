from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),#done
    path('login/', UserLogin, name='user_login'),#done
    path('register/', UserRegister, name='user_register'),#done
    path('encrypt/', upload_and_encrypt, name='encrypt'),#done
    path('list/', file_list, name= 'fileList'),
    path('list/<filename>', decrypt_and_download, name= 'decrypt'),
    path('logout/', UserLogout, name='user_logout')#done
]
