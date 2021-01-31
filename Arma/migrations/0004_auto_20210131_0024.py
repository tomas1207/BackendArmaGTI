# Generated by Django 3.1.4 on 2021-01-31 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Missions', '0001_initial'),
        ('Arma', '0003_auto_20210128_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kills',
            name='createdat',
        ),
        migrations.RemoveField(
            model_name='kills',
            name='updateat',
        ),
        migrations.RemoveField(
            model_name='medic',
            name='createdat',
        ),
        migrations.RemoveField(
            model_name='medic',
            name='updateat',
        ),
        migrations.RemoveField(
            model_name='shootsfired',
            name='createdat',
        ),
        migrations.RemoveField(
            model_name='shootsfired',
            name='updateat',
        ),
        migrations.AddField(
            model_name='kills',
            name='mission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_kills', to='Missions.missions'),
        ),
        migrations.AddField(
            model_name='medic',
            name='mission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_medic', to='Missions.missions'),
        ),
        migrations.AddField(
            model_name='shootsfired',
            name='mission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission', to='Missions.missions'),
        ),
        migrations.AddField(
            model_name='unconscious',
            name='mission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mission_unconscious', to='Missions.missions'),
        ),
    ]
