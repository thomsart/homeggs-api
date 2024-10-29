from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from account.models import User
from account.serializers import UserSerializer

from ..models import Company
from .company import CreateCompanySerializer, UpdateCompanySerializer, CompanySerializer
from ..models import ExceptionalExpense 
from .exceptional_expense import ExceptionalExpenseSerializer, CreateExceptionalExpenseSerializer, UpdateExceptionalExpenseSerializer
from ..models import Extra
from .extra import ExtraSerializer, CreateExtraSerializer, UpdateExtraSerializer
from ..models import FeeOrExpense
from .fee_or_expense import FeeOrExpenseSerializer
from ..models import Salary
from .salary import CreateSalarySerializer, SalarySerializer
from ..models import Saving
from .saving import SavingSerializer
from ..models import Tax
from .tax import TaxSerializer


__all__ = [
    "serializers", 
    "get_user_model", 
    "authenticate", 

    "User", 
    "UserSerializer", 

    "Company",
    "CreateCompanySerializer",
    "UpdateCompanySerializer",
    "CompanySerializer", 
    "ExceptionalExpense", 
    "ExceptionalExpenseSerializer", "CreateExceptionalExpenseSerializer", "UpdateExceptionalExpenseSerializer", 
    "Extra", "CreateExtraSerializer", "UpdateExtraSerializer", 
    "ExtraSerializer", 
    "FeeOrExpense", 
    "FeeOrExpenseSerializer", 
    "Salary", 
    "CreateSalarySerializer", 
    "SalarySerializer", 
    "Saving", 
    "SavingSerializer", 
    "Tax", 
    "TaxSerializer"
]
