from django.contrib.auth.models import User
from django.shortcuts import render
from property.models import Property, Place, Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post

def home(request):
  places = Place.objects.all().annotate(property_count=Count('property_place'))
  categories = Category.objects.all()

  #ToDo: get dynamic data 
  hotels_list = Property.objects.filter(category__name='Hotels')[:5]
  restaurants_list = Property.objects.filter(category__name='Restaurants')[:4]
  places_list = Property.objects.filter(category__name='Places')[:4]
  
  recent_posts = Post.objects.all()[:4]

  users_count = User.objects.all().count()
  hotels_count = Property.objects.filter(category__name='Hotels').count()
  restaurant_count = Property.objects.filter(category__name='Restaurants').count()
  places_count = Property.objects.filter(category__name='Places').count()

  context = {
    "places": places,
    "categories": categories,
    "hotels_list": hotels_list,
    "restaurants_list": restaurants_list,
    "places_list": places_list,
    "recent_posts": recent_posts,
    "users_count": users_count,
    "hotels_count": hotels_count,
    "restaurant_count": restaurant_count,
    "places_count": places_count,
   
   }
  return render(request, 'settings/home.html', context)


def home_search(request):
  name = request.GET.get('name')
  place = request.GET.get('place')
  property_list = Property.objects.filter(
    Q(name__icontains=name) & 
    Q(place__name__icontains=place) 
  )
  return render(request, 'settings/home_search.html', {"property_list": property_list})


def category_filter(request, category):
  category = Category.objects.get(name=category)
  property_list = Property.objects.filter(category=category) 

  return render(request, 'settings/home_search.html', {"property_list": property_list})


def contact_us(request):
  pass