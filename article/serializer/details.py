from django.contrib.auth.models import User
from rest_framework import serializers

from article.models import Article


class UserBaseDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ArticleDetailsSerializer(serializers.ModelSerializer):
    writer = UserBaseDetailsSerializer()

    class Meta:
        model = Article
        fields = '__all__'
