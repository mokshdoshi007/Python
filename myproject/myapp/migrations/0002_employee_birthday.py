# Generated by Django 3.1.1 on 2020-12-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='birthday',
            field=models.CharField(default=-2001, max_length=30),
            preserve_default=False,
        ),
    ]
