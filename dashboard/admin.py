from django.contrib import admin
from .models import Meal
from .models import History

# Register your models here.
admin.site.register(Meal)
admin.site.register(History)