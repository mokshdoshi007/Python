# Generated by Django 3.1.1 on 2021-01-05 11:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20210105_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='stars',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), blank=True, default=list, size=None),
        ),
    ]
