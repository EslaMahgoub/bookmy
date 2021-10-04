from django.urls import path
from .views import(
  PostByCategory,
  PostList,
  PostDetail,
  PostByCategory,
  PostByTags
)

from .api_view import(
  post_list_api,
  post_detail_api,
  post_search_api
)

app_name='blog'

urlpatterns = [
  path('', PostList.as_view(), name="post_list"),
  path('<slug:slug>', PostDetail.as_view(), name="post_detail"),
  path('category/<slug:slug>', PostByCategory.as_view(), name="post_by_category"),
  path('tag/<slug:slug>', PostByTags.as_view(), name="post_by_tag"),
  
  ##api
  path('api/list', post_list_api, name="post_list_api"),
  path('api/list/<int:id>', post_detail_api, name="post_detail_api"),
  path('api/list/filter/<str:query>', post_search_api, name="post_search_api")
] 
