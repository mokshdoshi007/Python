# Generated by Django 3.1.1 on 2020-12-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20201218_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='authToken',
            field=models.CharField(max_length=50),
        ),
    ]
