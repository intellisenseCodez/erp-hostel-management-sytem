# Generated by Django 3.2.9 on 2022-01-31 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20220131_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
    ]
