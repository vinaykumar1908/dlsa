# Generated by Django 4.2.11 on 2024-04-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shedin',
            name='RecordCreationDate',
        ),
        migrations.AddField(
            model_name='repairsection',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shedin',
            name='ShedInDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]