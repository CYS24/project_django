# Generated by Django 4.0.6 on 2022-07-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysb', '0003_member_alter_address_name_alter_brd_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]