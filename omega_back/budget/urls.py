from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import company, salary

budget_urlpatterns = [
    path('companies/', company.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', company.CompanyDetail.as_view(), name='company-detail'),
    path('salaries/', salary.SalaryList.as_view(), name='salary-list'),
    path('companies/<int:pk>/', salary.SalaryDetail.as_view(), name='salary-detail'),
]

budget_urlpatterns = format_suffix_patterns(budget_urlpatterns)