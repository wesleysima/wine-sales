
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from . import serializers
from rest_framework.views import APIView
from django.db import connections
import json, sys
from .services.client_service import sort_by_total_purchases, get_biggest_single_purchase, get_list_faithful_clients, get_client_wine_recommendation

class ClientsViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False, url_path='sort-by-total-purchases', url_name='sort-by-total-purchases')
    def order_by_total_purchases(self, request):

        data = sort_by_total_purchases()

        return Response(data)

    @action(methods=['get'], detail=False, url_path='biggest-single-purchase', url_name='biggest-single-purchase')
    def biggest_single_purchase(self, request):

        data = get_biggest_single_purchase()

        return Response(data)

    @action(methods=['get'], detail=False, url_path='list-faithful-clients', url_name='list-faithful-clients')
    def list_faithful_clients(self, request):

        data = get_list_faithful_clients()

        return Response(data)


    @action(methods=['get'], detail=False, url_path='(?P<client_id>.+)/wine-recommendation', url_name='wine-recommendation')
    def wine_recommendation(self, request, client_id):

        data = get_client_wine_recommendation(client_id)

        return Response(data)

            