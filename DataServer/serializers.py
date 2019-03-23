from rest_framework_mongoengine import serializers
from .models import GetData

class GetDataSerializer(serializers.DocumentSerializer):
    class Meta:
        model = GetData
        fields = '__all__'