# Generated by Django 3.2.9 on 2022-02-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_hostel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='no_dues',
            field=models.BooleanField(default=True),
        ),
    ]
