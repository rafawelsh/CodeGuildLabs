from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateField(blank=True)

    def toggle_todo(self):
        self.completed = not self.completed
        if self.completed:
            self.completed_date = timezone.now()
        else:
            self.completed_date = None
        self.save()

    def __str__(self):
        return self.text
