from django.db import models
from django.contrib.auth.admin import User
from django.urls import reverse

class Posts(models.Model):
    uploader = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=2500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts-detail", kwargs={"pk": self.pk})