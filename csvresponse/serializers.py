from rest_framework import serializers
from . import models
import pandas as pd

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    dataframe = serializers.SerializerMethodField('get_dataframe')


    def get_dataframe(self, obj):
        try:
            return pd.read_csv(obj['file'])
        except pd.errors.ParserError:
            raise serializers.ValidationError('wrong file format')

class DealsSerializer(serializers.ModelSerializer):
    index = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Deal
        fields = ['uuid','customer', 'item', 'total', 'quantity', 'date', 'index']

    def create(self, validated_data):
        return models.Deal.objects.create(**validated_data)


class TopCustomerSerializer(serializers.Serializer):
    spent_money = serializers.IntegerField()
    name = serializers.CharField()
    gems = serializers.SerializerMethodField('get_gems')

    def get_gems(self, obj):
        customer_gems = models.Deal.objects.filter(customer=obj['name']).values('item').distinct()
        gems = set()
        for cust in self.context['topnames']:
            if cust['name']==obj['name']:
                continue
            union = cust['customer_gems'].filter(item__in=customer_gems)
            gems.update([row['item'] for row in union])
        return gems
