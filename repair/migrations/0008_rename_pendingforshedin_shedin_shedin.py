# Generated by Django 4.2.11 on 2024-04-22 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0007_shedin_shedoutdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shedin',
            old_name='PendingForShedIn',
            new_name='ShedIn',
        ),
    ]
