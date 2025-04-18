"""
Module of budget/urls.py
"""


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    CompanyList, CompanyDetail, 
    SalaryList, SalaryDetail,
    ExceptionalExpenseList, ExceptionalExpenseDetail,
    ExtraList, ExtraDetail,
    FeeOrExpenseList, FeeOrExpenseDetail,
    SalaryList, SalaryDetail,
    SavingList, SavingDetail,
    TaxList, TaxDetail,
)

app_name = 'budget'

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('exceptional-expenses/', ExceptionalExpenseList.as_view(), name='exceptional-expense-list'),
    path('exceptional-expenses/<int:pk>/', ExceptionalExpenseDetail.as_view(), name='exceptional-expense-detail'),
    path('extras/', ExtraList.as_view(), name='extra-list'),
    path('extras/<int:pk>/', ExtraDetail.as_view(), name='extra-detail'),
    path('fee-or-expenses/', FeeOrExpenseList.as_view(), name='fee-or-expenses-list'),
    path('fee-or-expenses/<int:pk>/', FeeOrExpenseDetail.as_view(), name='fee-or-expenses-detail'),
    path('salaries/', SalaryList.as_view(), name='salary-list'),
    path('salaries/<int:pk>/', SalaryDetail.as_view(), name='salary-detail'),
    path('savings/', SavingList.as_view(), name='saving-list'),
    path('savings/<int:pk>/', SavingDetail.as_view(), name='saving-detail'),
    path('taxes/', TaxList.as_view(), name='tax-list'),
    path('taxes/<int:pk>/', TaxDetail.as_view(), name='tax-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)