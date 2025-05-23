from django.db import models
from user.models import User_Data

class Expenses(models.Model):

    class Category(models.TextChoices):
        PERSONAL = 'Personal', 'Personal'
        FRIENDS = 'Friends', 'Friends'
        FAMILY = 'Family', 'Family'

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=Category.choices, 
    )
    date=models.DateField()
    description = models.TextField()
    username = models.ForeignKey(User_Data, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - Rs. {self.amount} on {self.date} for {self.category}"