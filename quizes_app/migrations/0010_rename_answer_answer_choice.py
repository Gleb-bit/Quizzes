# Generated by Django 3.2.7 on 2021-09-30 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes_app', '0009_auto_20210930_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='choice',
        ),
    ]
