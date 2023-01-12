from rest_framework import serializers
from .models import Custom_auth
class CustomAuthSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=200, required=True)
    auth_token = serializers.UUIDField(required=True)

    class Meta:
        model = Custom_auth
        fields = ('__all__')

    def create(self, validated_data):
        return Custom_auth.objects.create(**validated_data)