"""
Module for tax views.
"""

from . import (
    APIView, permissions, Response, status, 
    Tax
)
from ..permissions import IsSuperuser, IsActive