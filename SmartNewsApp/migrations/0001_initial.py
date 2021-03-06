# Generated by Django 3.0.4 on 2020-03-10 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistic_code', models.IntegerField()),
                ('concept', models.TextField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartNewsApp.Date')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartNewsApp.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Enter source identification', max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=4)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartNewsApp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartNewsApp.Source')),
                ('publishedAt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartNewsApp.Date')),
                ('topics', models.ManyToManyField(related_name='news', to='SmartNewsApp.Topic')),
            ],
        ),
    ]
