# Generated by Django 3.1.1 on 2020-11-28 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_student',
            new_name='is_teacher',
        ),
    ]