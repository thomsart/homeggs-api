from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from account.models import User
from account.serializers import UserSerializer

from ..models import Coast
from .coast import CoastSerializer
from ..models import Product
from .product import ProductSerializer
from ..models import Shop
from .shop import ShopSerializer

__all__ = [
    "serializers", 
    "get_user_model", 
    "authenticate", 

    "User", 
    "UserSerializer", 

    "Coast", 
    "CoastSerializer", 
    "Product", 
    "ProductSerializer",  
    "Shop", 
    "ShopSerializer", 
]
