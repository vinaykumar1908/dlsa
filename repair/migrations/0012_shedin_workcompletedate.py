# Generated by Django 4.2.11 on 2024-04-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0011_remove_repairdetail_materialneeded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedin',
            name='WorkCompleteDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
