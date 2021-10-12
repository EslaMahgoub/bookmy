from django.urls import path
from .views import(
  PropertyList,
  PropertyDetail,
  PropertyCreate,
  property_by_category

)

from .api_view import(
  PropertyAPIList,
  PropertyAPIDetail,
)

app_name='property'

urlpatterns = [
  path('', PropertyList.as_view(), name="property_list"),
  path('new',PropertyCreate.as_view() , name='property_create' ),
  path('<slug:slug>', PropertyDetail.as_view(), name="property_detail"),
  path('category/<str:category>', property_by_category , name='property_by_category'),

  ##api
  path('api/list', PropertyAPIList.as_view(), name="property_list_api"),
  path('api/list/<int:pk>', PropertyAPIDetail.as_view(), name="property_detail_api"),
] 
