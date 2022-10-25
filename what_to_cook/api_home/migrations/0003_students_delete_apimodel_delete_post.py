# Generated by Django 4.1.2 on 2022-10-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_home', '0002_apimodel_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.IntegerField(max_length=40)),
                ('section', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='ApiModel',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
