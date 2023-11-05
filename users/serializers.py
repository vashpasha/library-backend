from django.contrib.auth import get_user_model
from rest_framework import serializers

from books.serializers import BookSmallSerializer

UserModel = get_user_model()


class UserSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'is_staff')


class UserDetailSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='userprofile.avatar', read_only=True)
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'is_staff', 'avatar', 'email')
