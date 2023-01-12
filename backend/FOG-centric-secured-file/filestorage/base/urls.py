from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('file/', file_list, name='filelist'),
    path('file/verify/<filename>', verify, name='verify'),
    path('file/verify/<filename>/delete', delete_file, name='delete'),
    path('file/verify/<filename>/download', download_file, name='download'),
    path('upload/', file_upload, name='fileUpload')
]

