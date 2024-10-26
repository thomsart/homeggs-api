from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from account.models import User
from account.serializers import UserSerializer

from ..models import (
    Coast,
    Company,
    ExceptionalExpense,
    Extra,
    FeeOrExpense,
    Product,
    Salary,
    Saving,
    Shop,
    Tax
)
from ..serializers import (
    CoastSerializer,
    CreateCompanySerializer, UpdateCompanySerializer, CompanySerializer,
    ExceptionalExpenseSerializer,
    ExtraSerializer,
    FeeOrExpenseSerializer,
    ProductSerializer,
    CreateSalarySerializer, SalarySerializer,
    SavingSerializer,
    ShopSerializer,
    TaxSerializer,
)
from .company import CompanyList, CompanyDetail
from .salary import SalaryList, SalaryDetail

__all__ = [
    "APIView",
    "permissions",
    "Response",
    "status",
    "Http404",

    "User",
    "UserSerializer",

    "Coast",
    "Company",
    "ExceptionalExpense",
    "Extra",
    "FeeOrExpense",
    "Product",
    "Salary",
    "Saving",
    "Shop",
    "Tax",

    "CoastSerializer", 
    "CreateCompanySerializer", "UpdateCompanySerializer", "CompanySerializer",
    "ExceptionalExpenseSerializer",
    "ExtraSerializer",
    "FeeOrExpenseSerializer",
    "ProductSerializer",
    "CreateSalarySerializer", "SalarySerializer",
    "SavingSerializer",
    "ShopSerializer",
    "TaxSerializer",

    "CompanyList", "CompanyDetail",
    "SalaryList", "SlaryDetail",
]