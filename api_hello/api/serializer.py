from rest_framework.serializers import ModelSerializer
from api.models import Filme

from rest_framework import serializers

class FilmeSerializer(ModelSerializer):

    class Meta:
        model = Filme
        fields = '__all__'

from django.contrib.auth import get_user_model
...

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user