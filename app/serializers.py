from rest_framework import serializers
from app.models import OrderForm


class OrderFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderForm
        fields = '__all__'

