from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from account.models import User
from account.permissions import IsSuperuser, IsStaff, IsActive
from account.serializers import UserSerializer

from ..models import (
    Coast,
    Product,
    Shop,
)
from ..serializers import (
    CoastSerializer,
    ProductSerializer, CreateProductSerializer, UpdateProductSerializer, 
    ShopSerializer,
)
# from .coast import CoastList, CoastDetail
from .product import ProductList, ProductDetail
# from .shop import ShopList, ShopDetail


__all__ = [
    "APIView",
    "permissions",
    "Response",
    "status",
    "Http404",

    "User", 
    "IsSuperuser", "IsStaff", "IsActive", 
    "UserSerializer",

    "Coast",
    "Product",
    "Shop",

    "CoastSerializer", 
    "ProductSerializer", "CreateProductSerializer", "UpdateProductSerializer", 
    "ShopSerializer",

    "ProductList", "ProductDetail",
]