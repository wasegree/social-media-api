from django.db import models


# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.TextField()
    online_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
