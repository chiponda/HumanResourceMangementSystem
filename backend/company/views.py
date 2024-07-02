

# Create your views here.
from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the CompanySerializer from the serializer file
from .serializers import CompanySerializer

# import the Company model from the models file
from .models import Company

# create a class for the Todo model viewsets
class CompanyView(viewsets.ModelViewSet):

	# create a serializer class and 
	# assign it to the TodoSerializer class
	serializer_class = CompanySerializer

	# define a variable and populate it 
	# with the Todo list objects
	queryset =Company.objects.all()
