from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.db.models import Sum, Max
from django.db.models import F

class CsvResponseAPIView(APIView):

    def get(self, request):
        deals = models.Deal.objects.all()
        serializer = serializers.DealsSerializer(deals, many=True)
        return Response(serializer.data)

    def post(self, request):
        fileserializer = serializers.FileSerializer(data=request.data)
        fileserializer.is_valid(raise_exception=True)
        deals = fileserializer.data['dataframe']
        index = models.Deal.get_last_index()+1
        for _, row in deals.iterrows():
            deal = row.to_dict()
            deal['index'] = index
            serializer = serializers.DealsSerializer(data=deal)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        print(deal)
        return Response({'status': 'success'}, status.HTTP_201_CREATED)


class TopCustomerAPIView(APIView):
    
    def get(self, request):
        deals = models.Deal.objects.filter(index=models.Deal.get_last_index())
        topcustomer = deals.values('customer').annotate(name=F('customer'),spent_money=Sum('total')).order_by('-spent_money')[:5]
        topnames = topcustomer.values('name')
        for top in topnames:
            top['customer_gems'] = models.Deal.get_customer_gems(top['name'])
        serializer = serializers.TopCustomerSerializer(topcustomer.values('spent_money', 'name'), context={'topnames':topnames}, many=True)
        return Response(serializer.data)