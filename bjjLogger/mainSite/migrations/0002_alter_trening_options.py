# Generated by Django 5.0.2 on 2024-02-24 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trening',
            options={'ordering': ['dateOfTraining']},
        ),
    ]