from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    owner = models.OneToOneField(
        User, unique=True, primary_key=True, on_delete=models.CASCADE
    )

    WRITER = 1
    EDITOR = 2
    ROLE_CHOICES = (
        (EDITOR, 'Editor'),
        (WRITER, 'Writer'),
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=WRITER,
        help_text='Writer = 1, Editor = 2')
