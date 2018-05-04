from rest_framework import serializers
from . import models


class HelloSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.Profile(
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
