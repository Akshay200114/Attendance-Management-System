# Generated by Django 3.1.2 on 2020-12-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0004_auto_20201203_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]