from rest_framework import serializers

from api_app.models import CartItem



class CartItemSerializer(serializers.ModelSerializer): #PascalCase
    #1 Properties
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    prouduct_qty = serializers.IntegerField(required=False, default=1)
    #2. Constructor
    
    
    #3. Method
    
    #4. Nested Class
    class Meta():
        model = CartItem
        fields = ('__all__')
        pass
    pass