from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterUserValidatorSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=[UnicodeUsernameValidator(),
                    UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    class Meta:
        model = User

    def validate(self, data):
        user = User(**data)
        password = data.get('password')

        errors = dict()
        try:
            password_validation.validate_password(password=password, user=user)
        except ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(RegisterUserValidatorSerializer, self).validate(data)
