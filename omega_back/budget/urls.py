from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CompanyList, CompanyDetail, 
    SalaryList, SalaryDetail
)

budget_urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('salaries/', SalaryList.as_view(), name='salary-list'),
    path('companies/<int:pk>/', SalaryDetail.as_view(), name='salary-detail'),
]

budget_urlpatterns = format_suffix_patterns(budget_urlpatterns)