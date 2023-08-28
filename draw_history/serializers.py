from rest_framework import serializers
from .models import DrawHistory

class DrawHistorySerializer(serializers.ModelSerializer):
    class Meta :
        model = DrawHistory
        fields = '__all__'