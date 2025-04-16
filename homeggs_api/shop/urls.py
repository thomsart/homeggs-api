from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    ProductList, ProductDetail,
)

shop_urlpatterns = [
    # path('coasts/', CoastList.as_view(), name='company-list'),
    # path('coasts/<int:pk>/', CoastDetail.as_view(), name='company-detail'),
    path('products/', ProductList.as_view(), name='salary-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='salary-detail'),
    # path('shops/', ShopList.as_view(), name='salary-list'),
    # path('shops/<int:pk>/', ShopDetail.as_view(), name='salary-detail'),
]

shop_urlpatterns = format_suffix_patterns(shop_urlpatterns)