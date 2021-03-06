# Generated by Django 3.2.7 on 2021-09-30 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes_app', '0008_rename_choice_choice_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='title',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.ManyToManyField(to='quizes_app.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='quizes_app.question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='title',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='', max_length=4096),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quizes_app.answer'),
        ),
    ]
