from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from config import settings
from api.services import get_rel_news
from api.schemes import request_body, response_ok


class GetRelativeData(generics.GenericAPIView):
    
    @swagger_auto_schema(
        request_body=request_body,  
        responses={
            200: response_ok,
        } 
    )
    def post(self, request) -> Response:
        data = request.data
        role = data['role']
        if role in settings.ROLES:
            news_list = get_rel_news(role=role)
            return Response({'relative_news': news_list}, status=status.HTTP_200_OK)
        return Response({'message': 'incorrect role'}, status=status.HTTP_400_BAD_REQUEST)
