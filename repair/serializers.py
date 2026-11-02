
from rest_framework import serializers
from repair.models import CustomerDb, RepairDb


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerDb
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepairDb
        fields = '__all__'
