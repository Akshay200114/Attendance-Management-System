# Generated by Django 3.1.2 on 2020-12-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0008_auto_20201213_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='Unique_id',
            field=models.IntegerField(),
        ),
    ]
