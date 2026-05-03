from django.contrib import admin
from .models import ParishProfile

@admin.register(ParishProfile)
class ParishProfileAdmin(admin.ModelAdmin):  # Tutaj była zmiana: ModelAdmin zamiast adminSite
    list_display = ('name', 'primary_color', 'background_color')