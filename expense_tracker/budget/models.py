from django.db import models
from user.models import User_Data

class Budget(models.Model):
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(User_Data, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username