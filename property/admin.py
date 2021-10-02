from django.contrib import admin

from .models import (
  Property, 
  PropertyImages, 
  Place, 
  Category, 
  PropertyReview, 
  PropertyBook)

admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)

