# Generated by Django 4.2.11 on 2024-04-21 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StaffName', models.CharField(max_length=100)),
                ('TokenNumber', models.IntegerField(blank=True, null=True)),
                ('Designation', models.CharField(blank=True, choices=[('SelectDesig', 'Please Select Designation '), ('Tech-1', 'Tech-1'), ('Tech-2', 'Tech-2'), ('Tech-3', 'Tech-3'), ('Sr.Tech', 'Sr.Tech'), ('MCM', 'MCM'), ('JE', 'JE'), ('SSE', 'SSE')], default='SelectDesig', max_length=11, null=True)),
                ('DOB', models.DateField(null=True)),
                ('LocoFailed', models.BooleanField(blank=True, default=False)),
                ('StaffFile', models.FileField(blank=True, null=True, upload_to='Staff/%Y/%m/%d/')),
                ('Staffimage', models.ImageField(default='default.jpg', upload_to='staff_profile_pics')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='staffauth1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
