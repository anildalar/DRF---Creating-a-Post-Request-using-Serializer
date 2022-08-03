from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_app.serializers import CartItemSerializer
from .models import CartItem
# Create your views here.


class CartItemViews(APIView):
    
    #3. Method area
    def post(self,request):
        print(request.data)
        serializer = CartItemSerializer(data = request.data)
        
        if serializer.is_valid():
            #True
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            #False
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        pass
    pass