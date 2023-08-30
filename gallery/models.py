from django.contrib.auth.models import User
from django.db import models


class photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
