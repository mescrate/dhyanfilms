from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    sender = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
      return self.name