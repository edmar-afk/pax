# Generated by Django 5.0.6 on 2024-07-04 01:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_student_parent_student_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='parent',
        ),
        migrations.AddField(
            model_name='attendance',
            name='parent',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
