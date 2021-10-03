from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from .forms import SignupForm, UserForm , ProfileForm
from .models import Profile
from property.models import PropertyBook, Property

# Create your views here.

class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('/')


class RegisterView(FormView):
  template_name = 'registration/register.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('/')

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super(RegisterView, self).form_valid(form)

  # prevent the user from going to /login or /register if he is logged in 
  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect("/")

    return super(RegisterView, self).get(*args, **kwargs)


def signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST or None)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password1 = form.cleaned_data.get('password1')
      user = authenticate(username=username, password1=password1)
      login(request, user)
      return redirect("/accounts/profile/")
  else:
    form = SignupForm()
  return render(request, 'registration/signup.html', {'form': form})


def profile(request):
  profile = Profile.objects.get(user=request.user)

  return render(request, 'profile/profile.html', {'profile': profile})


def edit_profile(request): 
  profile = Profile.objects.get(user=request.user)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      user_profile = profile_form.save(commit=False)
      user_profile.user = request.user
      user_profile.save()
      return redirect("profile")

  else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)

  context = {
    "user_form": user_form,
    "profile_form": profile_form,
      }


  return render(request, 'profile/profile_edit.html', context)


def my_reservation(request):
  reservation_list = PropertyBook.objects.filter(user=request.user)
  return render(request, 'profile/reservation.html', {'reservation_list': reservation_list} )

def my_listing(request):
  my_listing_list = Property.objects.filter(owner=request.user)
  return render(request, 'profile/my_listing.html', {'my_listing_list': my_listing_list} )