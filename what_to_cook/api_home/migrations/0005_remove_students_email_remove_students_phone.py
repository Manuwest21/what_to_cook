# Generated by Django 4.1.2 on 2022-10-25 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_home', '0004_alter_students_name_alter_students_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='email',
        ),
        migrations.RemoveField(
            model_name='students',
            name='phone',
        ),
    ]
