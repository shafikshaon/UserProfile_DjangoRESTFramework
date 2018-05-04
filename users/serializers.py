from rest_framework import serializers



class HelloSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
