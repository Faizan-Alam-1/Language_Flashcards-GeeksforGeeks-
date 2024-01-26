from django.contrib import admin
from .models import Addcard

@admin.register(Addcard)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'input_box', 'text_area']  # Customize the fields to display in the admin list view
    search_fields = ['input_box']  # Add fields for searching in the admin interface

