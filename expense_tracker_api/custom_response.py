from rest_framework.response import Response

class StandardResponseMixin:
    
    
    def finalize_response(self, request, response, *args, **kwargs):
        
        if response.status_code >= 200 and response.status_code < 300:
            if isinstance(response.data, (list, dict)):
                response.data = {
                    'status': 'success',
                    'data': response.data
                }
        return super().finalize_response(request, response, *args, **kwargs)