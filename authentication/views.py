from django.shortcuts import render
import os
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.utils import swagger_auto_schema
import logging
from .selializers import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
  
)


logger = logging.getLogger(__name__)




class CustomTokenObtainPairView(TokenObtainPairView):    
    serializer_class = CustomTokenObtainPairSerializer






class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
    
    
