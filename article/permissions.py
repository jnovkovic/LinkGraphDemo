from rest_framework import permissions

from article.models import Article
from user.models import Profile


class IsWriter(permissions.BasePermission):
    """
    Check if user have a role of a writer
    """
    def has_permission(self, request, view):
        profile = request.user.profile
        return  profile and profile.role == Profile.WRITER


class IsArticleOwner(permissions.BasePermission):
    """
    Check if user is set as a article writer
    """
    def has_permission(self, request, view):
        return Article.objects\
            .filter(pk=view.kwargs['article_id'],
                    writer=request.user,
                    status__in=[Article.NEW, Article.IN_REVIEW])\
            .exists()


class IsArticleOpenForApproval(permissions.BasePermission):
    """
    Check if user is editor and article is ready for review
    """
    def has_permission(self, request, view):
        profile = request.user.profile
        return profile and \
               profile.role == Profile.EDITOR and \
               Article.objects.\
                   filter(pk=view.kwargs['article_id'],
                          status=Article.IN_REVIEW).\
                   exists()
