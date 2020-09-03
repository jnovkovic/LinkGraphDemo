from django.db import transaction
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from article.models import Article
from article.permissions import IsWriter, IsArticleOwner, \
    IsArticleOpenForApproval
from article.serializer.details import ArticleDetailsSerializer
from article.serializer.validator.create_article import \
    ArticleCreateValidatorSerializer
from article.serializer.validator.google_doc_validator import \
    GoogleDocValidatorSerializer


class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleDetailsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all().select_related('writer')


class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleCreateValidatorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Article.objects.create(**serializer.validated_data)
            return Response(data={'message': 'Article created'},
                            status=status.HTTP_200_OK)


class ArticleAssignAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsWriter]

    def post(self, request, *args, **kwargs):
        queryset = Article.objects.select_for_update()\
            .filter(pk=kwargs['article_id'])
        with transaction.atomic():
            article = queryset[0]
            if article.writer_id:
                return Response(data={'message': 'Article already taken'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                article.writer = request.user
                article.save()
                return Response(data={'message': 'Article is assigned to you'},
                                status=status.HTTP_200_OK)


class ArticleReviewAPIView(CreateAPIView):
    serializer_class = GoogleDocValidatorSerializer
    permission_classes = [IsAuthenticated, IsArticleOwner]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article = Article.objects.get(pk=kwargs['article_id'])
            article.status = Article.IN_REVIEW
            article.content_url = serializer.validated_data['google_doc']
            article.save()
            return Response(data={'message': 'Article submited for review'},
                            status=status.HTTP_200_OK)


class ArticleApproveAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsArticleOpenForApproval]

    def post(self, request, *args, **kwargs):
        Article.objects.filter(pk=kwargs['article_id'])\
            .update(status=Article.APPROVED)
        return Response(data={'message': 'Article is approved'},
                        status=status.HTTP_200_OK)
