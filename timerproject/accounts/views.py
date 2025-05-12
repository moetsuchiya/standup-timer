from django.shortcuts import render
from django.contrib.auth.models import User #django.contrib.auth.modelsは元々djangoに入ってる！　userテーブルは元々あるから createsuperuserがいきなり出来る
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('clock')
# Create your views here.
