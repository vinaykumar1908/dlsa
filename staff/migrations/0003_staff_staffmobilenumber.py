# Generated by Django 4.2.11 on 2024-04-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_remove_staff_locofailed'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='StaffMobileNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
