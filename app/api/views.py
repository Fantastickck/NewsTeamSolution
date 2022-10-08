from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from config import settings
from api.services import get_rel_news


class GetRelativeData(generics.GenericAPIView):

    def post(self, request) -> None:
        data = request.data
        role = data['role']
        if role in settings.ROLES:
            news_list = get_rel_news(role=role)
            return Response({'relative_news': news_list}, status=status.HTTP_200_OK)
        return Response({'error': 'incorrect role'})
