from django.conf.urls import url

from .views import ArticleListAPIView, ArticleAssignAPIView, \
    ArticleReviewAPIView, ArticleApproveAPIView, ArticleCreateAPIView


urlpatterns = [
    url(r'^$', ArticleListAPIView.as_view()),
    url(r'^create/$', ArticleCreateAPIView.as_view()),
    url(r'^assign/(?P<article_id>[0-9]+)/$', ArticleAssignAPIView.as_view()),
    url(r'^review/(?P<article_id>[0-9]+)/$', ArticleReviewAPIView.as_view()),
    url(r'^approve/(?P<article_id>[0-9]+)/$', ArticleApproveAPIView.as_view()),
]
