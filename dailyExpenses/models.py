from django.db import models


class Parent(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=500)


class Child(models.Model):
    login = models.CharField(max_length=30)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, related_name="children")


class Category(models.Model):
    name = models.CharField(max_length=30)


class Plan(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="plans")
    price = models.FloatField()
    date = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    confirm = models.BooleanField(default=False)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='plans')
