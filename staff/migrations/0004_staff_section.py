# Generated by Django 4.2.11 on 2024-04-22 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_alter_section_sectionincharge'),
        ('staff', '0003_staff_staffmobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='StaffSection', to='section.section'),
        ),
    ]
