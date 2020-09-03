from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    writer = models.ForeignKey(
        User, blank=True, null=True, related_name='user_articles',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    content_url = models.URLField(blank=True, null=True)

    NEW = 1
    IN_REVIEW = 2
    APPROVED = 3
    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_REVIEW, 'In review'),
        (APPROVED, 'Approved'),
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=NEW,
        help_text='New = 1, In review = 2, Approved = 3')
