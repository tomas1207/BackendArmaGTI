# Generated by Django 3.1.4 on 2021-05-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='user_name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='vestName',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
