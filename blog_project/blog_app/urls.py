from django.contrib import admin
from django.urls import path

# views
from . import views
from .views import home, resume, PostDetailView, PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='blog-home'),
    path('resume/', resume, name='blog-resume'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
    path('about/', views.about, name='blog-about'),
]
