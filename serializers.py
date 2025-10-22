from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField()

class DataSerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.JSONField()