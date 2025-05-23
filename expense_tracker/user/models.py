from django.db import models

class User_Data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return ""
