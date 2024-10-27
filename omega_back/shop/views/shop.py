"""
Module for shop views.
"""

from . import (
    APIView, permissions, Response, status, 
    Shop
)
from ..permissions import IsSuperuser, IsActive