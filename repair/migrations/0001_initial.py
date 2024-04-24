# Generated by Django 4.2.11 on 2024-04-22 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section', '0002_section_sectionincharge'),
        ('holding', '0008_delete_loco'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocoFile', models.FileField(blank=True, null=True, upload_to='LocoShedIn/%Y/%m/%d/')),
                ('RecordCreationDate', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('LocoNumber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='holding.loco2')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locoauth14', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RepairSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_comment', models.BooleanField(default=False)),
                ('LocoNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ccomments', to='repair.shedin')),
                ('RepSection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='section.section')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locoauth15', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RepairDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('commentfile', models.FileField(blank=True, null=True, upload_to='RepairFile/%Y/%m/%d/')),
                ('RepSection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bcomments', to='repair.repairsection')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locoauth16', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]