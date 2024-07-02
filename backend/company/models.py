from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=100)
    departments = models.CharField(max_length=500)  # Comma-separated list of departments
    num_employees = models.IntegerField()
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
 
        #it will return the title
          return self.name