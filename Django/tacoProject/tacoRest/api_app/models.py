from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=254)
    lang = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    page_title = models.CharField(max_length=254)
    page_number = models.IntegerField()
    page_position = models.IntegerField()
    currency = models.CharField(max_length=10)

    def __str__(self):
        return '{} : {}'.format(self.name, self.lang)


class Comment(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    content = models.TextField()
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return 'comment from: {}, for: {}'.format(self.menu_item, self.name)
