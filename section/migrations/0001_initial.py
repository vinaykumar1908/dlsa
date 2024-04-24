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
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SectionName', models.CharField(max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sectionauth1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]