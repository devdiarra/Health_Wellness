from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    prof = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class history(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField()
    date_publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.name} | {self.text[:20]} ...'
