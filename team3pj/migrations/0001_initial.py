# Generated by Django 4.0.6 on 2022-08-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('rdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worldcup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=200)),
            ],
        ),
    ]
