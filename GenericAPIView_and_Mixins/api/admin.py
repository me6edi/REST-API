from django.contrib import admin
from .models import Studnet
# Register your models here.


@admin.register(Studnet)

class StudnetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']