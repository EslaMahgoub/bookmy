from django.shortcuts import redirect, render

from django.views.generic import ListView, DetailView
from .models import Property
from django.views.generic.edit import FormMixin, CreateView

from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView

class PropertyList(FilterView):
  model = Property
  context_object_name = 'property_list'
  paginate_by = 1
  filterset_class = PropertyFilter
  template_name = 'property/property_list.html'

  #filter
  #pagination
  
class PropertyDetail(FormMixin, DetailView):
  model = Property
  form_class = PropertyBookForm

  def get_context_data(self, **kwargs):
    context = super(PropertyDetail, self).get_context_data(**kwargs)
    context["related_property"] = Property.objects.filter(category=self.get_object().category)[:2]
    return context

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
      new_form = form.save(commit=False)
      new_form.property = self.get_object()
      new_form.user = request.user
      new_form.save()
    
    return redirect(" ")

  # book

class AddListing(CreateView):
  pass