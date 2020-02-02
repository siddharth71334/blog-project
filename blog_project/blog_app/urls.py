from django.contrib import admin
from django.urls import path

# views
from . import views
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='blog-home')
    # path('/resume', resume, name='blog-resume')
]
