from django.contrib import admin
from .models import Chronicle

@admin.register(Chronicle)
class ChronicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_headline')
    prepopulated_fields = {'slug': ('title',)}

    