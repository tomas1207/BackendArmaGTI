# Generated by Django 3.1.4 on 2021-06-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_campaign_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
