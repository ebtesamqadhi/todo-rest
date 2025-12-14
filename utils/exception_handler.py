from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "success": False,
            "status_code": response.status_code,
            "error": response.data
        }, status=response.status_code)

    if isinstance(exc, Http404):
        return Response({
            "success": False,
            "status_code": 404,
            "error": "Not found."
        }, status=status.HTTP_404_NOT_FOUND)

    return Response({
        "success": False,
        "status_code": 500,
        "error": "Internal server error"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
