# Generated by Django 3.1.1 on 2020-09-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('scontact', models.IntegerField()),
                ('semail', models.EmailField(max_length=254)),
                ('scity', models.CharField(max_length=30)),
            ],
        ),
    ]
