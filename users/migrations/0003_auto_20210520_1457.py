# Generated by Django 3.1.4 on 2021-05-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210510_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
