from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Property, Category, PropertyImages, PropertyReview
from django.views.generic.edit import FormMixin, CreateView

from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView

class PropertyList(FilterView):
  model = Property
  context_object_name = 'property_list'
  paginate_by = 4
  filterset_class = PropertyFilter
  template_name = 'property/property_list.html'
  
class PropertyDetail(FormMixin, DetailView):
  model = Property
  form_class = PropertyBookForm

  def get_context_data(self, **kwargs):
    context = super(PropertyDetail, self).get_context_data(**kwargs)
    context["related_property"] = Property.objects.filter(category=self.get_object().category)[:2]
    context['review_count'] = PropertyReview.objects.filter(property=self.get_object()).count()
    return context

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    print(form)
    if form.is_valid():
      print('form inside if is_valid', form)
      new_form = form.save(commit=False)
      new_form.property = self.get_object()
      new_form.user = request.user
      new_form.save()
      messages.success(request, 'Your Reservation Confirmed')
    
    return redirect(reverse('property:property_detail' , kwargs={'slug':self.get_object().slug}))

  # book
class PropertyCreate(CreateView):
    model = Property
    fields = ['name','description','price','place','image', 'category']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
          myform = form.save(commit=False)
          myform.owner = request.user
          myform.save()
          messages.success(request, 'Successfully Added Your Property')
          ### send gmail message
          return redirect(reverse('property:property_list'))

def property_by_category(request,category):
    my_category = Category.objects.get(name=category)
    property_categroy = Property.objects.filter(category=my_category)
    return render(request , 'property/property_by_category.html' , {'property_categroy':property_categroy , 'my_category':my_category})