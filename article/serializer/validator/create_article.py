from rest_framework import serializers


class ArticleCreateValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
