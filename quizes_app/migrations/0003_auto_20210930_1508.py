# Generated by Django 3.2.7 on 2021-09-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes_app', '0002_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='max_points',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='visible',
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('текст', 'ответ текстом'), ('один вариант', 'ответ с выбором одного варианта'), ('несколько вариантов', 'ответ с выбором нескольких вариантов')], default='текст', max_length=255),
        ),
    ]
