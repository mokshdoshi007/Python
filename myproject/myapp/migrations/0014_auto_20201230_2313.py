# Generated by Django 3.1.1 on 2020-12-30 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20201230_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='favturfs',
            new_name='favturf',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='stars',
            new_name='ratings',
        ),
    ]
