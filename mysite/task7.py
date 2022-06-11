#task7.py 
#kodeCamp assignment
#import product model
from home.models import Product

#Insert new record into a product model
New_entry = Product(product_name = "Paracetamol", quantity = 50, price = 23.9 )
New_entry.save()

#Get all records in a product table
Product.objects.all()

#filter products by their name
Product.objects.filter(product_name = "Procold")

#filter products by their name
Product.objects.get(product_name = "Procold")

#Change a product price 
test = Product.objects.get(product_name = "Amoxil")
test.price = 1000
test.save()