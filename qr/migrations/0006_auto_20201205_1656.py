# Generated by Django 3.1.2 on 2020-12-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0005_student_qr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('Subject', models.CharField(choices=[['AOS', 'Advanced Operating System'], ['CN', 'Computer Networks'], ['WDL', 'Web Design Lab'], ['MP', 'Microprocessor'], ['DBMS', 'DataBase Management System'], ['TCS', 'Theory Of Computer Science']], max_length=40)),
                ('Unique_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='sem',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
