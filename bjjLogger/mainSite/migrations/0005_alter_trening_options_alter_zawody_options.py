# Generated by Django 5.0.2 on 2024-03-03 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0004_zawody_compfight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trening',
            options={'ordering': ['-dateOfTraining']},
        ),
        migrations.AlterModelOptions(
            name='zawody',
            options={'ordering': ['-dateOfComp']},
        ),
    ]
