from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from account.models import User
from account.serializers import UserSerializer
from account.permissions import IsActive, IsSuperuser

from ..models import (
    Company,
    ExceptionalExpense,
    Extra,
    FeeOrExpense,
    Salary,
    Saving,
    Tax
)
from ..serializers import (
    CreateCompanySerializer, UpdateCompanySerializer, CompanySerializer,
    ExceptionalExpenseSerializer, CreateExceptionalExpenseSerializer, UpdateExceptionalExpenseSerializer, 
    ExtraSerializer, CreateExtraSerializer, UpdateExtraSerializer, 
    FeeOrExpenseSerializer, CreateFeeOrExpenseSerializer, UpdateFeeOrExpenseSerializer, 
    CreateSalarySerializer, UpdateSalarySerializer, SalarySerializer,
    CreateSavingSerializer, UpdateSavingSerializer, SavingSerializer,
    TaxSerializer,CreateTaxSerializer, UpdateTaxSerializer,
)
from .company import CompanyList, CompanyDetail
from .exceptional_expense import ExceptionalExpenseList, ExceptionalExpenseDetail
from .extra import ExtraList, ExtraDetail
from .fee_or_expense import FeeOrExpenseList, FeeOrExpenseDetail
from .salary import SalaryList, SalaryDetail
from .saving import SavingList, SavingDetail
from .tax import TaxList, TaxDetail


__all__ = [
    "APIView", 
    "permissions", 
    "Response", 
    "status", 
    "Http404", 

    "User", 
    "UserSerializer", 
    'IsActive', 'IsSuperuser', 

    "Company", 
    "ExceptionalExpense", 
    "Extra", 
    "FeeOrExpense", 
    "Salary", 
    "Saving", 
    "Tax", 

    "CompanySerializer", "CreateCompanySerializer", "UpdateCompanySerializer", 
    "ExceptionalExpenseSerializer", "CreateExceptionalExpenseSerializer", "UpdateExceptionalExpenseSerializer", 
    "ExtraSerializer", "CreateExtraSerializer", "UpdateExtraSerializer", 
    "FeeOrExpenseSerializer", "CreateFeeOrExpenseSerializer", "UpdateFeeOrExpenseSerializer", 
    "SalarySerializer", "UpdateSalarySerializer", "CreateSalarySerializer", 
    "SavingSerializer", "CreateSavingSerializer", "UpdateSavingSerializer", 
    "TaxSerializer", "CreateTaxSerializer", "UpdateTaxSerializer", 

    "CompanyList", "CompanyDetail", 
    "ExceptionalExpenseList", "ExceptionalExpenseDetail", 
    "ExtraList", "ExtraDetail", 
    "FeeOrExpenseList", "FeeOrExpenseDetail", 
    "SalaryList", "SalaryDetail", 
    "SavingList", "SavingDetail", 
    "TaxList", "TaxDetail", 
]