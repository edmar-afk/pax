# Generated by Django 5.0.6 on 2024-07-03 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_attendance_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='year',
        ),
    ]
