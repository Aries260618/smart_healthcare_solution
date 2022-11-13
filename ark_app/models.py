from django.db import models
import django.utils.timezone as timezone

# Create your models here.

gender_choice = (
    ('m','male'),
    ('f','female')
)

class Degree(models.Model):
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 'degree'

    def __str__(self):
        return self.Name

class Doctor(models.Model):
    image = models.ImageField(upload_to = 'doctors/images/')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=15,choices=gender_choice)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20,null=True)
    pin = models.IntegerField(null=True)
    mobile = models.CharField(max_length=10,null=True)
    dob = models.DateField(auto_created = True,null=True,default=timezone.now)
    description = models.TextField(max_length=255,null=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    clinic_name = models.CharField(max_length=50)
    clinic_address = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

class Patient(models.Model):
    image = models.ImageField(upload_to = 'patients/images/')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.name