# Generated by Django 4.2.11 on 2024-04-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opr', '0002_alter_opr_loconumber_alter_opr_detantion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opr',
            name='detantion_time',
            field=models.DurationField(null=True),
        ),
    ]
