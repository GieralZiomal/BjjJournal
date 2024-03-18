# Generated by Django 5.0.2 on 2024-03-18 18:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('belt', models.CharField(choices=[('White', 'White'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('Brown', 'Brown'), ('Black', 'Black'), ('Red', 'Red')], max_length=10, verbose_name='User Belt')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfTraining', models.DateField()),
                ('hourOfTraining', models.TimeField()),
                ('trainingDuration', models.IntegerField()),
                ('typeOfWorkout', models.CharField(choices=[('no-gi', 'NO-GI'), ('gi', 'GI')], max_length=5)),
                ('howManyFights', models.IntegerField()),
                ('fightDuration', models.IntegerField()),
                ('breakDuration', models.IntegerField()),
                ('tiredAfter', models.IntegerField()),
                ('injuriesAfter', models.CharField(max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dateOfTraining'],
            },
        ),
        migrations.CreateModel(
            name='Zawody',
            fields=[
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
                ('nameOfComp', models.CharField(max_length=20)),
                ('dateOfComp', models.DateField()),
                ('place', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dateOfComp'],
            },
        ),
        migrations.CreateModel(
            name='CompFight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultOfFight', models.CharField(choices=[('Win', 'W'), ('Lose', 'L')], max_length=10)),
                ('endOfFight', models.CharField(choices=[('Submission', 'SUB'), ('Points', 'PO'), ('Disqualification', 'DQ'), ('Choice', 'CHO')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compFight', to=settings.AUTH_USER_MODEL)),
                ('whichComp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comp_fights', to='mainSite.zawody')),
            ],
        ),
    ]
