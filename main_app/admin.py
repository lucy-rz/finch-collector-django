from django.contrib import admin
from .models import Finch, Feeding, Toy

# Register your models here.
admin.site.register([Finch, Feeding, Toy])