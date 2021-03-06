# Generated by Django 3.1.2 on 2020-12-13 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0009_auto_20201213_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('roll_no', models.PositiveIntegerField()),
                ('subject', models.CharField(max_length=64)),
                ('Mis_no', models.PositiveIntegerField()),
                ('Department', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
