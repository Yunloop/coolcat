# Generated by Django 2.2.5 on 2019-09-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20190919_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='body_html',
            field=models.TextField(default='', verbose_name='HTML格式正文'),
        ),
        migrations.AddField(
            model_name='article',
            name='body_md',
            field=models.TextField(default='', verbose_name='Markdown格式正文'),
        ),
    ]
