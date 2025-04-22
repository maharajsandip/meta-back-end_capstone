from django.contrib import admin
from .models import menu
from .models import booking


# Register your models here.
admin.site.register(menu)
admin.site.register(booking)