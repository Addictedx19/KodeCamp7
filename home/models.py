from django.db import models

# Create your models here.
class People(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
        
    def __str__(self):
        return self.username

class Address(models.Model):
    house_add = models.CharField(max_length=1000)
    city = models.CharField(max_length= 100)
    state = models.CharField(max_length= 100)
    People = models.ForeignKey(People, on_delete= models.CASCADE)

    def __str__(self):
        return self.house_add

class Bio(models.Model):
    bio = models.CharField(max_length=1000)
    People = models.OneToOneField(People, on_delete= models.CASCADE)    

    def __str__(self):
        return self.bio

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    People = models.ForeignKey(People, on_delete= models.CASCADE)    

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length= 200)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product_name