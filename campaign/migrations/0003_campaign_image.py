# Generated by Django 3.1.4 on 2021-05-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_campaign_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
