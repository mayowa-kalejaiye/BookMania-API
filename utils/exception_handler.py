# myproject/exception_handler.py

from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler
    response = exception_handler(exc, context)

    if response is not None:
        # Add custom fields or modify the response as needed
        response.data['custom_error'] = 'A custom error message'

    return response
