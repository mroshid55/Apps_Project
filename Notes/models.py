from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices

# Create your models here.


class Note(models.Model):
    Select_value1 = (('note-personal', 'Personal'), ('note-work', 'Work'),
                     ('note-social', 'Social'), ('note-important', 'Important'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, default='Untitled')
    description = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=25, choices=Select_value1)
    favourites = models.BooleanField(default=False)
