from django.contrib import admin
from django.urls import include, path

from api_app.views import CartItemViews

urlpatterns = [
    path('cart-items/', CartItemViews.as_view())
]


#  /api + /cart-item ->  /api/cart-items