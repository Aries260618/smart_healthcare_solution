from django.contrib import admin
from .models import *

admin.site.site_header = admin.site.site_title = "Ark Medical"

# Register your models here.


admin.site.register(Degree)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)