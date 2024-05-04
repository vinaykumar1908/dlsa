# Generated by Django 4.2.11 on 2024-04-30 21:15

from django.db import migrations, models
import staff.models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_alter_staff_tokennumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='TokenNumber',
            field=models.IntegerField(default=staff.models.random_string, unique=True),
        ),
    ]
