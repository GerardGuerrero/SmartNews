# Generated by Django 3.0.4 on 2020-05-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartNewsApp', '0004_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.TextField(default='title'),
        ),
    ]
