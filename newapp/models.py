from django.db import models

# Create your models here.
# This is Customer model.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.name