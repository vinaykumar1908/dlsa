# Generated by Django 4.2.11 on 2024-04-30 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('repair', '0012_shedin_workcompletedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedin',
            name='PresentLocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='locations.locations'),
        ),
    ]
