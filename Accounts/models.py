from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    nickname = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to="Picture", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height >= 90 or img.weight >= 90:
            output_size = (90, 90)
            img.thumbnail(output_size)
            img.save(self.image.path)
