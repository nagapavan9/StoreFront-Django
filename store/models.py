from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # we need to use string instead of class name if the parent class is below the child class
    collection = models.ForeignKey("Collection", on_delete=models.PROTECT())

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'BRONZE'),
        (MEMBERSHIP_SILVER,'SILVER'),
        (MEMBERSHIP_GOLD,'GOLD')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_CHOICES = [
        (PAYMENT_PENDING,'PENDING'),
        (PAYMENT_COMPLETED, 'COMPLETED'),
        (PAYMENT_FAILED, 'FAILED')
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT())
    product = models.ForeignKey(Product, on_delete=models.PROTECT())
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE())

class Collection(models.Model):
    title = models.CharField(max_length=255)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE())
    product = models.ForeignKey(Product, on_delete=models.CASCADE())
    quantity = models.PositiveSmallIntegerField()

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE())
    cart = models.ForeignKey(Order, on_delete=models.CASCADE())


