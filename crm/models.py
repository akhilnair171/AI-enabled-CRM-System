from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    vendor = models.CharField(max_length=200, null=True)
    discount = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=(
        ('CANCELED', 'CANCELED'),
        ('COMPLETED', 'COMPLETED'),
        ('REFUNDED', 'REFUNDED'),
        ('PENDING PAYMENT', 'PENDING PAYMENT'),
    ))


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.text


class Lead(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    cust_probability = models.CharField(max_length=100, null=True, choices=(
        ('YES', 'YES'),
        ('NO', 'NO'),
    ))
    priority = models.CharField(max_length=200, null=True, choices=(
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    ))

    def __str__(self):
        return self.name


class SentimentModel(models.Model):
    Sentence = models.CharField(max_length=120)
