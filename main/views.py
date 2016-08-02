from django.shortcuts import render
from django.views import generic

from .models import Category

# Create your views here.
class IndexView(generic.ListView):
    model = Category
    template_name = 'main/index.html'
