from rest_framework import serializers
from .models import Productss
class ProductSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای مدل Product
    """
    class Meta:
        model = Productss
        fields = '__all__'  # تمام فیلدهای مدل را در سریالایزر شامل می‌شود.