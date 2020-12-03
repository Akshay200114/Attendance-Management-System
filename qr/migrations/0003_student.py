# Generated by Django 3.1.2 on 2020-12-03 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_auto_20201128_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('Roll_no', models.PositiveIntegerField()),
                ('Dept', models.CharField(max_length=64)),
                ('Mis_no', models.PositiveIntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['Roll_no'],
            },
        ),
    ]