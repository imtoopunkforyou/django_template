from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from charity.models import Charity
from charity.serializers import CharitySerializer


class CharityViewSet(viewsets.ViewSet):

    @swagger_auto_schema()
    @action(detail=False, methods=['GET'])
    def all_list(self, request):
        """
        Test connection
        :return:
        
        """
        return Response(data={CharitySerializer.data}, status=status.HTTP_200_OK)
