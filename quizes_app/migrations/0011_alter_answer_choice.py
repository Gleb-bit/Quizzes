# Generated by Django 3.2.7 on 2021-09-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes_app', '0010_rename_answer_answer_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ManyToManyField(blank=True, to='quizes_app.Choice'),
        ),
    ]
