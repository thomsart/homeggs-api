"""
Module for product views.
"""

from . import (
    APIView, permissions, Response, status, 
    Product
)
from ..permissions import IsSuperuser, IsActive