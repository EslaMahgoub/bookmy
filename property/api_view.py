from .models import Property
from .serializers import PropertySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models.query_utils import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView


class PropertyAPIList(ListAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer

class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer


