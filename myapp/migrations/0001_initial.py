# Generated by Django 5.1 on 2024-09-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('medical_condition', models.CharField(max_length=20)),
                ('accidental_history', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
