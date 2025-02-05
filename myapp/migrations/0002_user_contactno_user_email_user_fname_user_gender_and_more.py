# Generated by Django 5.1 on 2024-09-06 06:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contactno',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='fname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lname',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='accidental_history',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='medical_condition',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
