from django.urls import path,include
from .views import case_index, add_crime, add_crime_form

urlpatterns = [
    path("",case_index, name='crime_home'),
    path("add/",add_crime_form, name='crime_add')
]