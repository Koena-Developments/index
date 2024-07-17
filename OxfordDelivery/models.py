from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    allow_live_location = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.user.name}'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.item.item_name} in order {self.order.id}'
