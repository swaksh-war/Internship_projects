from django.urls import path,include
from .views import criminal_index, add_criminal

urlpatterns = [
    path("",criminal_index, name='criminal_home'),
    path("add/", add_criminal, name='criminal_add')

]