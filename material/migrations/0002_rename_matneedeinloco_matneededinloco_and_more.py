# Generated by Django 4.2.11 on 2024-04-27 21:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_alter_section_sectionincharge'),
        ('repair', '0010_shedin_locofaildate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MatNeedeInLoco',
            new_name='MatNeededInLoco',
        ),
        migrations.RenameField(
            model_name='matneededinloco',
            old_name='LocoFile',
            new_name='MaterialFile',
        ),
    ]