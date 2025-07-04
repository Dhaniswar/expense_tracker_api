from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.core.exceptions import FieldError

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)
    
    # Handle specific exceptions
    if isinstance(exc, ValidationError):
        return Response({
            'status': 'error',
            'code': 'validation_error',
            'message': 'Validation failed',
            'errors': exc.detail
        }, status=status.HTTP_400_BAD_REQUEST)
    
    elif isinstance(exc, IntegrityError):
        return Response({
            'status': 'error',
            'code': 'integrity_error',
            'message': 'Database integrity error occurred',
            'detail': str(exc)
        }, status=status.HTTP_400_BAD_REQUEST)
    
    elif isinstance(exc, FieldError):
        return Response({
            'status': 'error',
            'code': 'field_error',
            'message': 'Invalid field operation',
            'detail': str(exc)
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # If no specific handler, use default response or create a generic one
    if response is not None:
        response.data = {
            'status': 'error',
            'code': response.status_code,
            'message': 'An error occurred',
            'detail': response.data
        }
    else:
        response = Response({
            'status': 'error',
            'code': 'server_error',
            'message': 'Internal server error occurred',
            'detail': str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return response