from django.db import models

# Create your models here.

# items in a resturant
class Items:
    itemsID = models.ForeignKey(Resturant, on_delete=models.CASCADE)


class Order:
    OrderId= models.ForeignKey(Items, on_delete=models.CASCADE)
    UserId= models.ForeignKey(Items, on_delete=models.CASCADE)
    Resturant=models.ForeignKey(Items, on_delete=models.CASCADE)



class User:
    Userid = models.ForeignKey(Order, on_delete=models.CASCADE)
    Name = models.CharField(max_length= 200)
    Surname = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    AllowLiveLocation = models.BooleanField(False)


class Resturant:
    ResturantId = models.ForeignKey(Items, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Orders = models.IntegerField()








