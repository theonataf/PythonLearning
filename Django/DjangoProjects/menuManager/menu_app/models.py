from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=254)
    price = models.CharField(max_length=254)

    def __str__(self):
        return '{} : {}'.format(self.name, self.price)
