# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Company

# create a serializer class
class CompanySerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Company
		fields = ("name","registration_date","registration_number","address","contact_person","departments","num_employees","contact_phone","email")

