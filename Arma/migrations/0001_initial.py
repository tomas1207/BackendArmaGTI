# Generated by Django 3.1.4 on 2021-02-23 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Missions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='unconscious',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField()),
                ('createdat', models.DateTimeField()),
                ('updateat', models.DateTimeField()),
                ('mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_unconscious', to='Missions.missions')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Uncoscious', to=settings.AUTH_USER_MODEL, to_field='steamID')),
            ],
        ),
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
                ('mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission', to='Missions.missions')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit', to=settings.AUTH_USER_MODEL, to_field='steamID')),
            ],
        ),
        migrations.CreateModel(
            name='medic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hitLocation', models.TextField()),
                ('typeOfHeal', models.TextField()),
                ('healed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='healed', to=settings.AUTH_USER_MODEL, to_field='steamID')),
                ('healer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='healer', to=settings.AUTH_USER_MODEL, to_field='steamID')),
                ('mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_medic', to='Missions.missions')),
            ],
        ),
        migrations.CreateModel(
            name='kills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.TextField(default=0)),
                ('killed', models.TextField(default=0)),
                ('distance', models.TextField(default=0)),
                ('killer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='killer', to=settings.AUTH_USER_MODEL, to_field='steamID')),
                ('mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_kills', to='Missions.missions')),
            ],
        ),
    ]
