# Generated by Django 3.1.4 on 2021-06-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_campaign_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.ImageField(default='Fenix_v2.png', upload_to='images/'),
        ),
    ]
