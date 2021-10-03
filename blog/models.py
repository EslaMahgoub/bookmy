from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  tags = TaggableManager()
  image = models.ImageField(upload_to="post/")
  description = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
  slug = models.SlugField(null=True, blank=True)


  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    return super(Post, self).save(*args, **kwargs)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("blog:post_detail", kwargs={'slug': self.slug})

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
