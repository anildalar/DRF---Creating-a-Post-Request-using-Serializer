from django.db import models

# Create your models here.

class CartItem(models.Model): # PascalCase
    #1. Property
    # propertyname = value
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    prouduct_qty = models.PositiveIntegerField() # 0 ---->
    
    #2. Constuctor
    
    #3. MEthod
    
    #4. Nesteed Class
    pass