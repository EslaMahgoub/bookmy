from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  tags = TaggableManager()
  image = models.ImageField(upload_to="post/")
  description = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  category = models.ForeignKey('Category', models.CASCADE)

  def __str__(self):
    return self.title

class Category(models.Model):
  name = models.CharField(max_length=50)
