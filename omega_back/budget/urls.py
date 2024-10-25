from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import company_views, salary_views

budget_urlpatterns = [
    path('companies/', company_views.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', company_views.CompanyDetail.as_view(), name='company-detail'),
    path('salaries/', salary_views.SalaryList.as_view(), name='salary-list'),
    path('companies/<int:pk>/', salary_views.SalaryDetail.as_view(), name='salary-detail'),
]

budget_urlpatterns = format_suffix_patterns(budget_urlpatterns)