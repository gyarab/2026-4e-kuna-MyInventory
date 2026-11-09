from django.db import models

class ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50) #jednotka, ve ktere je ingredience merena (napr. gram, kilogram, litr, kus)
    expiration_date = models.DateField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
# Create your models here.
