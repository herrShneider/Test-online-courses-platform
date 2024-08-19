from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    # TODO

    class Meta:
        model = Subscription
        fields = (
            # TODO
            'course',
            'student',
        )

    def to_representation(self, instance):
        """Изменяем представление данных."""
        representation = super().to_representation(instance)
        representation['course'] = str(instance.course)
        representation['student'] = str(instance.student)
        return representation
