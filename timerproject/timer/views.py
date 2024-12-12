from django.shortcuts import render
from django.views.generic import ListView
from .models import StudyRecord

class ListTimerView(ListView):
    template_name = 'timer/timer_list.html'
    model = StudyRecord
# Create your views here.
