from django.db import models
from django.contrib.auth.models import User

class MissingPerson(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    last_seen_location = models.CharField(max_length=255)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    # username = models.CharField(max_length=150, editable=False)

    # def save(self, *args, **kwargs):
    #     if self.created_by:
    #         self.username = self.created_by.username  # Store username
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name
