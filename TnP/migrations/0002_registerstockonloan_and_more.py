# Generated by Django 4.2.11 on 2024-04-22 10:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staff_staffmobilenumber'),
        ('TnP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerStockOnLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=100)),
                ('PL_Number', models.IntegerField()),
                ('stockDispatched', models.IntegerField()),
                ('updateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('StaffName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='StaffNameTnP', to='staff.staff')),
            ],
        ),
        migrations.DeleteModel(
            name='registerStockDispatchedROH',
        ),
    ]
