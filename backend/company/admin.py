from django.contrib import admin

# Register your models here.

from django.contrib import admin

# import the model Todo
from .models import Company

# create a class for the admin-model integration
class CompanyAdmin(admin.ModelAdmin):

	# add the fields of the model here
	list_display = ("name","registration_date","registration_number","address","contact_person","departments","num_employees","contact_phone","email")

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Company,CompanyAdmin)
