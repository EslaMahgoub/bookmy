from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import (
  CustomLoginView,
  RegisterView,
  signup,
  profile,
  edit_profile,
  my_reservation,
  my_listing
)
app_name="accounts"

urlpatterns = [
    # path('login/', CustomLoginView.as_view(), name="login"),
    # path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', profile, name="profile"),
    path('profile/edit/', edit_profile, name="profile_edit"),
    path('signup/', signup, name="signup"),
    path('reservation/', my_reservation, name="my_reservation"),
    path('my_listing/', my_listing, name="my_listing"),
] 
