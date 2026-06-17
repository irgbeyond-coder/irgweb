from django.contrib import admin
from .models import AutomationTask

@admin.register(AutomationTask)
class AutomationTaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_type', 'status', 'files_processed', 'completed_at')

    