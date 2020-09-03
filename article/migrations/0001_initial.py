# Generated by Django 3.1.1 on 2020-09-03 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content_url', models.URLField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'New'), (2, 'In review'), (3, 'Approved')], default=1, help_text='New = 1, In review = 2, Approved = 3')),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
