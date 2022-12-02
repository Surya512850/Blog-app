from django.shortcuts import render
from django.views import generic
from .forms import SignupForm
from django.urls import reverse_lazy

# Create your views here.
class UserRegister(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
