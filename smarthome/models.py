from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30)
    is_performed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
