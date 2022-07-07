import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Msg = models.TextField()

    def __str__(self):
        return self.Fname
