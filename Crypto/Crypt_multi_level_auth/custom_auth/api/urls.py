from django.urls import path
from .views import AuthView

urlpatterns = [
    path('basic/', AuthView.as_view()),
    path('basic/<str:user>/<str:auth_token>', AuthView.as_view()),
]
