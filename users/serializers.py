from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ['is_staff', 'is_active']


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError({'inactive account': msg})
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError({'wrong_credentials': msg})
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError({'blank input': msg})

        data['user'] = user
        return data