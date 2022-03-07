from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=10)


class Parent(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="parent")
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=500)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class Child(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="child")
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=500, default="")
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, related_name="children")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


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
