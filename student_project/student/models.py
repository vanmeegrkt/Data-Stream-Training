# model class represents structure of the table
# By referring to model class, Django can automatically create the table in database.

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name