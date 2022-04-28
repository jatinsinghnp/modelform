from django.contrib import admin
from .models import Model1

# Register your models here.
@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    list_display = ("id", "name", "address")
