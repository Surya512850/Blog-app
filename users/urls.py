from django.urls import path,include
from .views import UserRegister
urlpatterns = [
path('register/',view = UserRegister.as_view(),name='register'),
]
