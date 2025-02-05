# Generated by Django 5.1 on 2024-10-21 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_usersession'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=100)),
                ('scheduled_time', models.TimeField()),
                ('message_log', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userdet')),
            ],
        ),
        migrations.DeleteModel(
            name='UserSession',
        ),
    ]
