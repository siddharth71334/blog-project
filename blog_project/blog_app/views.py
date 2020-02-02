from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Posts
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)

# Create your views here.
def home(request):
    return render(request, template_name='home.html')

def resume(request):
    return 

def about(request):
    """
    Displays about page requests.
    """
    title = {'title': 'About'} 
    return render(request, template_name='about.html', context=title)

class PostListView(ListView):
    """
    Orders the homepage in a better (list) view
    """
    model = Posts
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']