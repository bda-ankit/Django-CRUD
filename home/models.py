from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField()
    file = models.FileField


class Product(models.Model):
    pass