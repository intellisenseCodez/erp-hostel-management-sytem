# Generated by Django 3.2.9 on 2022-02-06 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_student_hostel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='hostel',
        ),
    ]