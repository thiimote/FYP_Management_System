# Generated by Django 3.0.2 on 2020-01-31 17:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0002_auto_20200128_1525'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='FinalProject',
        ),
    ]
