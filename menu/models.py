from django.db import models
from django.urls import reverse
# Create your models here.


class Menu(models.Model):
    MENU_CHOICES = (
        ('Starters','Starters'),
        ('Main', 'Main'),
        ('Breads', 'Breads'),
        ('Italian', 'Italian'),
        ('Dessert', 'Desssert'),
        ('Specials','specials'),
    )
    item_type = models.CharField(choices=MENU_CHOICES,default='All',max_length=20)
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=6)
    item_description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("menu:menu_list")

    def __str__(self):
        return self.item_name
