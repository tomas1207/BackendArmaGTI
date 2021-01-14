# Generated by Django 3.1.4 on 2021-01-14 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='shootsfired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.TextField()),
                ('muzzle', models.TextField()),
                ('mode', models.TextField()),
                ('ammo', models.TextField()),
                ('magazine', models.TextField()),
                ('projectile', models.TextField()),
                ('vehicle', models.TextField()),
                ('unit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]