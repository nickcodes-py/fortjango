from django.db import models

# Create your models here.

class Product(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    product_title = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_desc = models.TextField()
    product_link = models.TextField()
    product_bg = models.TextField()
    product_skin = models.TextField()

    def __str__(self):
        return self.product_title