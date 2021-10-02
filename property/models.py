from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Property(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='property/')
  price = models.IntegerField(default=0)
  description = models.TextField()
  place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE )
  category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class PropertyImages(models.Model):
  property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
  image = models.ImageField(upload_to='propertyimages/')

  def __str__(self):
    # return self.property.name
    return str(self.property)

class Place(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='places/')

  def __str__(self):
    return self.name


class Category(models.Model):
  name= models.CharField(max_length=40)

  def __str__(self):
    return self.name

class PropertyReview(models.Model):
  author = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
  property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
  rate = models.IntegerField(default=0)
  feedback = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return str(self.property)


COUNT = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
]
class PropertyBook(models.Model):
  user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
  property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
  date_from = models.DateField(default=timezone.now)
  date_to = models.DateField(default=timezone.now)
  guest = models.CharField(choices=COUNT, max_length=2)
  children = models.CharField(choices=COUNT, max_length=2)

  def __str__(self):
    return str(self.property)


