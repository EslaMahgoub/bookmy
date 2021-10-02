from django.db import models


class Settings(models.Model):
  site_name = models.CharField(max_length=50)
  logo = models.ImageField(upload_to='settings/')
  phone = models.CharField(max_length=20)
  email = models.EmailField(max_length=255)
  description = models.TextField()
  fb_link = models.URLField(max_length=255)
  twitter_link = models.URLField(max_length=255)
  instagram_link = models.URLField(max_length=255)

  def __str__(self):
    return self.site_name