from django.db import models
from model_utils.managers import InheritanceManager


class Order(models.Model):
    pass


class OrderItem(models.Model):
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    objects = InheritanceManager()


class Food(OrderItem):
    category = models.CharField(
        choices=(
            ('starter', 'starter'),
            ('main', 'main'),
            ('dessert', 'dessert')
        ),
        max_length=100, default='starter')


class Drink(OrderItem):
    capacity = models.IntegerField()


class Hard(Drink):
    time = models.CharField(
        choices=(
            ('pre-dinner', 'pre-dinner'),
            ('dinner', 'dinner'),
            ('post-dinner', 'post-dinner'),
            ('all-round', 'all-round')
            ),
        max_length=100, default='starter')


class Soft(Drink):
    category = models.CharField(
        choices=(
            ('hot', 'hot'),
            ('cold', 'cold'),
            ),
        max_length=100, default='cold')


class StrongAlcool(Hard):
    type = models.CharField(
        choices=(
            ('white', 'white'),
            ('brown', 'brown'),
            ('other', 'other'),
            ),
        max_length=100, default='white')


class Beer(Hard):
    genre = models.CharField(
        choices=(
            ('white', 'white'),
            ('pale', 'pale'),
            ('IPA', 'IPA'),
            ('Belgium', 'Belgium'),
            ),
        max_length=100, default='pale')


class FruitJuice(Soft):
    fruit = models.CharField(
        choices=(
            ('melon', 'melon'),
            ('strawberry', 'strawberry'),
            ('orange', 'orange'),
            ('lemon', 'lemon'),
            ),
        max_length=100, default='lemon')


class Soda(Soft):
    manufacturer = models.CharField(
        choices=(
            ('pepsi', 'pepsi'),
            ('coca', 'coca'),
            ('inhouse', 'inhouse'),
            ('other', 'other'),
            ),
        max_length=100, default='pepsi')
