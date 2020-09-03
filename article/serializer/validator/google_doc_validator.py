from django.core.validators import RegexValidator
from rest_framework import serializers


class GoogleDocValidatorSerializer(serializers.Serializer):
    google_doc = serializers.URLField(
        validators=[
            RegexValidator(regex='^https://docs.google.com/([a-zA-Z0-9-_]+)',
                           message='Wrong url')
        ]
    )
