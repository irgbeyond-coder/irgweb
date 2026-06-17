from django.db import models

class AutomationTask(models.Model):
    TASK_TYPES = [
        ('CLASSIFY', 'AI Classification'),
        ('ORGANIZE', 'File Organization'),
        ('OLLAMA', 'Ollama Query'),
    ]

    task_name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    status = models.CharField(max_length=20, default='Pending')
    files_processed = models.IntegerField(default=0)
    logs = models.TextField(blank=True)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name} ({self.task_type})"
    
    