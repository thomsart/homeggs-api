from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CompanyList, CompanyDetail, 
    SalaryList, SalaryDetail,
    ExceptionalExpenseList, ExceptionalExpenseDetail,

)

budget_urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('salaries/', SalaryList.as_view(), name='salary-list'),
    path('salaries/<int:pk>/', SalaryDetail.as_view(), name='salary-detail'),
    path('exceptional-expenses/', ExceptionalExpenseList.as_view(), name='exceptional-expense-list'),
    path('exceptional-expenses/<int:pk>/', ExceptionalExpenseDetail.as_view(), name='exceptional-expense-detail'),
]

budget_urlpatterns = format_suffix_patterns(budget_urlpatterns)