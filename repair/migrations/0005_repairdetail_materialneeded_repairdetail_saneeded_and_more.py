# Generated by Django 4.2.11 on 2024-04-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0004_rename_approved_comment_repairdetail_workcomplete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairdetail',
            name='MaterialNeeded',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='repairdetail',
            name='SANeeded',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='repairdetail',
            name='ShuntingNeeded',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='repairdetail',
            name='waitingForMaterial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repairdetail',
            name='waitingForSA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repairdetail',
            name='waitingForShunting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shedin',
            name='ShedOut',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shedin',
            name='workComplete',
            field=models.BooleanField(default=False),
        ),
    ]
