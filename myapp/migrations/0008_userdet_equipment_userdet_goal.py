# Generated by Django 5.1 on 2024-10-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_userdet_accidental_history_alter_userdet_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdet',
            name='equipment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userdet',
            name='goal',
            field=models.CharField(choices=[('weight_gain', 'Weight Gain'), ('weight_loss', 'Weight Loss'), ('strength_training', 'Strength Training')], default='weight_loss', max_length=30),
        ),
    ]
