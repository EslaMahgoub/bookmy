from django.contrib import admin

from .models import (
  Property, 
  PropertyImages, 
  Place, 
  Category, 
  PropertyReview, 
  PropertyBook)
  
from django_summernote.admin import SummernoteModelAdmin
class PropertyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)

