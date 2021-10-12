from .models import Property
from .serializers import PropertySerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.db.models.query_utils import Q
from rest_framework.permissions import IsAuthenticated

class PropertyAPIList(ListAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  permission_classes = [IsAuthenticated]

class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  permission_classes = [IsAuthenticated]


