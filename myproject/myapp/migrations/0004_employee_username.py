# Generated by Django 3.1.1 on 2020-12-07 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201206_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='now', max_length=30),
            preserve_default=False,
        ),
    ]
