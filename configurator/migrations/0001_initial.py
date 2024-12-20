# Generated by Django 5.1.4 on 2024-12-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_place', models.CharField(max_length=100)),
                ('train_type', models.CharField(max_length=100)),
                ('train_program', models.CharField(blank=True, max_length=100, null=True)),
                ('day_week', models.JSONField(blank=True, null=True)),
                ('muscle_groups', models.JSONField(blank=True, null=True)),
                ('difficulty', models.CharField(max_length=100)),
                ('train_config', models.JSONField(blank=True, null=True)),
                ('completedDays', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]