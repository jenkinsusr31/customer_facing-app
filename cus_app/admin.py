from django.contrib import admin

#from customer_facing_proj.cus_app.models import Customer
from .models import Customer

# Register your models here.

admin.site.register(Customer)