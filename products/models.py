from django.db import models

# Create your models here.
class Products(models.Model):
    index = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=255)
    titles = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    reviews = models.CharField(max_length=255)
    ratings = models.IntegerField()

    class Meta:
        db_table = 'products'