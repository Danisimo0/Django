from django.db import models


class Todo(models.Model):
    objects = None
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
