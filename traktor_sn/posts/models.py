from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    """
    A user-created post. Posts are displayed on the website home page
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:17] + '...' if len(str(self.title)) > 20 else self.title
