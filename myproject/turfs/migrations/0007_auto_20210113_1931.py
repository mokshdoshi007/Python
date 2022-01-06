# Generated by Django 3.1.1 on 2021-01-13 14:01

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210105_1643'),
        ('turfs', '0006_auto_20210110_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfs',
            name='sourceprice',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='turfs',
            name='sourceslots',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='turfs',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='myapp.users'),
        ),
    ]